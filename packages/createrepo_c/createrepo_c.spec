%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

%global libmodulemd_version 2.3.0

%define __cmake_in_source_build 1

%global bash_completion %{_datadir}/bash-completion/completions/*

%if ( 0%{?rhel} && ( 0%{?rhel} <= 7 || 0%{?rhel} >= 9 ) ) || ( 0%{?fedora} && 0%{?fedora} >= 39 )
%bcond_with drpm
%else
%bcond_without drpm
%endif

# Our EL8 buildroots default to Python 3.9, but let's also build 3.6, just to be safe
%if 0%{?rhel} == 8
%bcond_without python36
%else
%bcond_with python36
%endif

%if 0%{?rhel}
%bcond_with zchunk
%else
%bcond_without zchunk
%endif

%if 0%{?rhel} && 0%{?rhel} < 7
%bcond_with libmodulemd
# dnf supports zstd since 8.4: https://bugzilla.redhat.com/show_bug.cgi?id=1914876
%bcond_with zstd 
%else
%bcond_without libmodulemd
%bcond_without zstd
%endif

%if 0%{?rhel} && 0%{?rhel} <= 9
%bcond_without legacy_hashes
%else
%bcond_with legacy_hashes
%endif

%bcond_with sanitizers

Summary:        Creates a common metadata repository
Name:           createrepo_c
Version:        1.1.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/createrepo_c
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  file-devel
BuildRequires:  glib2-devel >= 2.22.0
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel >= 4.8.0-28
BuildRequires:  sqlite-devel >= 3.6.18
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zstd
%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= 0.9.11
BuildRequires:  zchunk
%endif
%if %{with libmodulemd}
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  libmodulemd2
Requires:       libmodulemd2%{?_isa} >= %{libmodulemd_version}
%else
BuildRequires:  libmodulemd
Requires:       libmodulemd%{?_isa} >= %{libmodulemd_version}
%endif
%endif
Requires:       %{name}-libs =  %{version}-%{release}
BuildRequires:  bash-completion
Requires: rpm >= 4.9.0
%if %{with drpm}
BuildRequires:  drpm-devel >= 0.4.0
%endif
# dnf supports zstd since 8.4: https://bugzilla.redhat.com/show_bug.cgi?id=1914876
BuildRequires:  pkgconfig(libzstd)

%if %{with sanitizers}
BuildRequires:  libasan
BuildRequires:  liblsan
BuildRequires:  libubsan
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
Obsoletes:      createrepo < 0.11.0
Provides:       createrepo = %{version}-%{release}
%endif

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package libs
Summary:    Library for repodata manipulation

%description libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package devel
Summary:    Library for repodata manipulation
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python 3 bindings for the createrepo_c library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
Requires:       %{name}-libs = %{version}-%{release}
%if 0%{?scl:1}
Obsoletes:      python3-%{name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{name} < %{version}-%{release}
Obsoletes:      python39-%{name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{name}
Python 3 bindings for the createrepo_c library.

%if %{with python36}
%package -n python3-%{name}
Summary:        Python 3 bindings for the createrepo_c library
BuildRequires:  python36-devel
Provides:       python36-%{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-%{name}
Python 3 bindings for the createrepo_c library.

%endif

%prep
%autosetup -p1
%py3_shebang_fix examples/python
mkdir build-py3
%if %{with python36}
mkdir build-py36
%endif

# it can't detect our special PYTHONPATH 
sed -i "/PYTHON_UNSET()/d" src/python/CMakeLists.txt

%build
set -ex
# Build createrepo_c with Pyhon 3
pushd build-py3
  %cmake .. \
      -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
      -DWITH_LIBMODULEMD=%{?with_libmodulemd:ON}%{!?with_libmodulemd:OFF} \
      -DWITH_LEGACY_HASHES=%{?with_legacy_hashes:ON}%{!?with_legacy_hashes:OFF} \
      -DWITH_ZSTD=%{?with_zstd:ON}%{!?with_zstd:OFF} \
      -DENABLE_DRPM=%{?with_drpm:ON}%{!?with_drpm:OFF} \
      -DPYTHON_EXECUTABLE=%{__python3} -DPYTHON_LIBRARY=/usr/lib64/libpython3.11.so
  make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"
  # Build C documentation
  make doc-c
popd

%if %{with python36}
# Build createrepo_c with Python 3.6
pushd build-py36
  %cmake .. \
      -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
      -DWITH_LIBMODULEMD=%{?with_libmodulemd:ON}%{!?with_libmodulemd:OFF} \
      -DENABLE_DRPM=%{?with_drpm:ON}%{!?with_drpm:OFF} \
      -DWITH_LEGACY_HASHES=ON \
      -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
      -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
      -DPYTHON_LIBRARY=/usr/lib64/libpython3.6m.so
  make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"
popd
%endif

%check
# Run Python 3 tests
pushd build-py3
  # Compile C tests
  make tests

  # Run Python 3 tests
  make ARGS="-V" test
popd

%install
set -ex
pushd build-py3
  # Install createrepo_c with Python 3
  make install DESTDIR=%{buildroot}
popd

%if %{with python36}
pushd build-py36
  # Install createrepo_c with Python 3.6
  make install DESTDIR=%{buildroot}
popd
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
ln -sr %{buildroot}%{_bindir}/createrepo_c %{buildroot}%{_bindir}/createrepo
ln -sr %{buildroot}%{_bindir}/mergerepo_c %{buildroot}%{_bindir}/mergerepo
ln -sr %{buildroot}%{_bindir}/modifyrepo_c %{buildroot}%{_bindir}/modifyrepo
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%else
%ldconfig_scriptlets libs
%endif

%files
%doc README.md
%{_mandir}/man8/createrepo_c.8*
%{_mandir}/man8/mergerepo_c.8*
%{_mandir}/man8/modifyrepo_c.8*
%{_mandir}/man8/sqliterepo_c.8*
%{bash_completion}
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c

%if 0%{?fedora} || 0%{?rhel} > 7
%{_bindir}/createrepo
%{_bindir}/mergerepo
%{_bindir}/modifyrepo
%endif

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc build-py3/doc/html
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%files -n python%{python3_pkgversion}-%{name}
%doc examples/python/*
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info

%if %{with python36}
%files -n python3-%{name}
/usr/lib64/python3.6/site-packages/%{name}/
/usr/lib64/python3.6/site-packages/%{name}-%{version}-py*.egg-info
%endif

%changelog
* Wed Jul 03 2024 Odilon Sousa <osousa@redhat.com> - 1.1.3-1
- Release createrepo_c 1.1.3

* Wed Apr 24 2024 Odilon Sousa <osousa@redhat.com> - 1.0.2-6
- Enable Legacy Hashes for EL9 builds

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 1.0.2-5
- Obsolete python39-createrepo_c as well

* Thu Nov 16 2023 Patrick Creech <pcreech@redhat.com> - 1.0.2-4
- Add in egg info for python 3.11

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.3-2
- Build against python 3.11

* Mon Nov 06 2023 Odilon Sousa <osousa@redhat.com> - 1.0.2-2
- Build python3.6 using python3 naming for EL8

* Fri Nov 03 2023 Odilon Sousa <osousa@redhat.com> - 1.0.2-1
- Release createrepo_c 1.0.2

* Mon Oct 23 2023 Odilon Sousa <osousa@redhat.com> - 1.0.1-1
- Release createrepo_c 1.0.1

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 0.20.1-1
- Release createrepo_c 0.20.1

* Tue May 24 2022 Odilon Sousa <osousa@redhat.com> - 0.20.0-2
- Bump package release for a rebuild on python 3.9

* Tue May 24 2022 Odilon Sousa - 0.20.0-1
- Release createrepo_c 0.20.0

* Thu May 12 2022 Yanis Guenane <yguenane@redhat.com> - 0.17.7-8.1
- Fix obsolete named package

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.17.7-7.1
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 29 2022 Odilon Sousa <osousa@redhat.com> - 0.17.7-6.1
- Bumping the release to rebuild against 3.9 on EL8

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 0.17.7-5.1
- Rebuilding against python 3.9

* Wed Mar 02 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.17.7-4.1
- Include patches from CentOS 8 Stream
- Fix memory leak of `tmp_err` (RhBug:2005781)
- Switch default of --keep-all-metadata to TRUE and add --discard-additional-metadata (RhBug:1992209)

* Tue Jan 04 2022 Evgeni Golov - 0.17.7-3.2
- Rebuild createrepo_c once more

* Mon Jan 03 2022 Evgeni Golov - 0.17.7-3.1
- Bump createrepo_c to be greater than CentOS

* Wed Dec 15 2021 Evgeni Golov - 0.17.7-1
- Release createrepo_c 0.17.7

* Wed Oct 27 2021 Evgeni Golov - 0.17.6-4
- Also build createrepo_c against Python 3.6 on EL8

* Tue Oct 26 2021 Evgeni Golov - 0.17.6-3
- Obsolete non-SCL Python 3 packages on EL7

* Tue Oct 05 2021 Evgeni Golov - 0.17.6-2
- Build against Python 3.8

* Tue Sep 28 2021 Evgeni Golov - 0.17.6-1
- Release createrepo_c 0.17.6

* Wed Mar 03 2021 Evgeni Golov - 0.17.1-1
- Release createrepo_c 0.17.1

* Thu Feb 18 2021 Justin Sherrill <jsherril@redhat.com> 0.17.0-1
- update to 0.17.0

* Wed Nov 11 2020 Justin Sherrill <jsherril@redhat.com> 0.16.2-1
* update to 0.16.2

* Thu Oct 01 2020 Evgeni Golov - 0.16.1-1
- Release createrepo_c 0.16.1

* Mon May 04 2020 Evgeni Golov - 0.15.10-1
- update to upstream 0.15.10
