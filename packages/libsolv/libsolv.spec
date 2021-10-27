# explicitly define, as we build on top of an scl, not inside with scl_package
%if 0%{?scl:1}
%global scl_prefix %{scl}-
%global python3_sitearch /opt/theforeman/tfm-pulpcore/root/usr/lib64/python3.8/site-packages/
%global python3_version %python38python3_version
%global __os_install_post %python38_os_install_post
%global __python_requires %python38_python_requires
%global __python_provides %python38_python_provides
%global __python3 %python38__python
%endif

# Our EL8 buildroots default to Python 3.8, but let's also build 3.6, just to be safe
# to make dnf happy
%if 0%{?rhel} == 8
%bcond_without python36
%else
%bcond_with python36
%endif

%global libname solv

# Only build Python2 bindings on EL7
%if 0%{?rhel} == 7
%bcond_without python2_bindings
%else
%bcond_with python2_bindings
%endif

%bcond_without python3_bindings
%bcond_with    perl_bindings
%bcond_without ruby_bindings
# Creates special prefixed pseudo-packages from appdata metadata
%bcond_without appdata
# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
# For rich dependencies
%bcond_without complex_deps
%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo
# For handling deb + rpm at the same time
%bcond_without multi_semantics
%bcond_with    zchunk
%bcond_with    zstd

Name:           lib%{libname}
Version:        0.7.20
Release:        4%{?dist}
Summary:        Package dependency solver

License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel
# -DWITH_LIBXML2=ON
BuildRequires:  libxml2-devel
# -DENABLE_LZMA_COMPRESSION=ON
BuildRequires:  xz-devel
# -DENABLE_BZIP2_COMPRESSION=ON
BuildRequires:  bzip2-devel
%if %{with zstd}
# -DENABLE_ZSTD_COMPRESSION=ON
BuildRequires:  libzstd-devel
%endif
%if %{with zchunk}
# -DENABLE_ZCHUNK_COMPRESSION=ON
BuildRequires:  pkgconfig(zck)
%endif

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rpm-devel%{?_isa}

%description devel
Development files for %{name}.

%package tools
Summary:        Package dependency solver tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# repo2solv dependencies. Used as execl()
Requires:       %{_bindir}/find

%description tools
Package dependency solver tools.

%package demo
Summary:        Applications demoing the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
# solv dependencies. Used as execlp() and system()
Requires:       %{_bindir}/curl
Requires:       %{_bindir}/gpg2

%description demo
Applications demoing the %{name} library.

%if %{with perl_bindings}
%package -n perl-%{libname}
Summary:        Perl bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  perl-devel
BuildRequires:  perl-generators
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{libname}
Perl bindings for the %{name} library.
%endif

%if %{with ruby_bindings}
%package -n ruby-%{libname}
Summary:        Ruby bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{libname}
Ruby bindings for the %{name} library.
%endif

%if %{with python2_bindings}
%package -n python2-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python2-%{libname}}
BuildRequires:  swig
BuildRequires:  python2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python2-%{libname}
Python bindings for the %{name} library.

Python 2 version.
%endif

%if %{with python3_bindings}
%package -n %{?scl_prefix}python%{python3_pkgversion}-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{libname}}
BuildRequires:  swig
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?scl:1}
Obsoletes:      python3-%{libname} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%if %{with python36}
%package -n python3-%{libname}
Summary:        Python bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  python36-devel
Provides:       python36-%{libname} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1

# it can't detect our special PYTHONPATH and uses the compiled-in from the SCL Python
%if 0%{?scl:1}
sed -i "/OUTPUT_VARIABLE PYTHON3_INSTALL_DIR/ s#))#).replace('rh/rh-python38', 'theforeman/tfm-pulpcore'))#" bindings/python3/CMakeLists.txt
%endif
%{?scl:EOF}

%if %{with python36}
mkdir build-py36
%endif

%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%cmake . -B"%{_vpath_builddir}" -GNinja          \
  -DFEDORA=1                                     \
  -DENABLE_RPMDB=ON                              \
  -DENABLE_RPMDB_BYRPMHEADER=ON                  \
  -DENABLE_RPMDB_LIBRPM=ON                       \
  -DENABLE_RPMPKG_LIBRPM=ON                      \
  -DENABLE_RPMMD=ON                              \
  %{?with_comps:-DENABLE_COMPS=ON}               \
  %{?with_appdata:-DENABLE_APPDATA=ON}           \
  -DUSE_VENDORDIRS=ON                            \
  -DWITH_LIBXML2=ON                              \
  -DENABLE_LZMA_COMPRESSION=ON                   \
  -DENABLE_BZIP2_COMPRESSION=ON                  \
  %{?with_zstd:-DENABLE_ZSTD_COMPRESSION=ON}     \
%if %{with zchunk}
  -DENABLE_ZCHUNK_COMPRESSION=ON                 \
  -DWITH_SYSTEM_ZCHUNK=ON                        \
%endif
  %{?with_helix_repo:-DENABLE_HELIXREPO=ON}      \
  %{?with_suse_repo:-DENABLE_SUSEREPO=ON}        \
  %{?with_debian_repo:-DENABLE_DEBIAN=ON}        \
  %{?with_arch_repo:-DENABLE_ARCHREPO=ON}        \
  %{?with_multi_semantics:-DMULTI_SEMANTICS=ON}  \
  %{?with_complex_deps:-DENABLE_COMPLEX_DEPS=1}  \
  %{?with_perl_bindings:-DENABLE_PERL=ON}        \
  %{?with_ruby_bindings:-DENABLE_RUBY=ON}        \
%if %{with python2_bindings} || %{with python3_bindings}
  -DENABLE_PYTHON=ON                             \
%if %{with python2_bindings}
  -DPYTHON_EXECUTABLE=%{__python2}               \
%if %{with python3_bindings}
  -DENABLE_PYTHON3=ON                            \
  -DPYTHON3_EXECUTABLE=%{__python3}              \
%endif
%else
  -DPYTHON_EXECUTABLE=%{__python3}               \
%endif
%endif
  %{nil}
%ninja_build -C "%{_vpath_builddir}"
%{?scl:EOF}

%if %{with python36}
pushd build-py36
%cmake .. -B"%{_vpath_builddir}" -GNinja         \
  -DFEDORA=1                                     \
  -DENABLE_RPMDB=ON                              \
  -DENABLE_RPMDB_BYRPMHEADER=ON                  \
  -DENABLE_RPMDB_LIBRPM=ON                       \
  -DENABLE_RPMPKG_LIBRPM=ON                      \
  -DENABLE_RPMMD=ON                              \
  %{?with_comps:-DENABLE_COMPS=ON}               \
  %{?with_appdata:-DENABLE_APPDATA=ON}           \
  -DUSE_VENDORDIRS=ON                            \
  -DWITH_LIBXML2=ON                              \
  -DENABLE_LZMA_COMPRESSION=ON                   \
  -DENABLE_BZIP2_COMPRESSION=ON                  \
  %{?with_zstd:-DENABLE_ZSTD_COMPRESSION=ON}     \
%if %{with zchunk}
  -DENABLE_ZCHUNK_COMPRESSION=ON                 \
  -DWITH_SYSTEM_ZCHUNK=ON                        \
%endif
  %{?with_helix_repo:-DENABLE_HELIXREPO=ON}      \
  %{?with_suse_repo:-DENABLE_SUSEREPO=ON}        \
  %{?with_debian_repo:-DENABLE_DEBIAN=ON}        \
  %{?with_arch_repo:-DENABLE_ARCHREPO=ON}        \
  %{?with_multi_semantics:-DMULTI_SEMANTICS=ON}  \
  %{?with_complex_deps:-DENABLE_COMPLEX_DEPS=1}  \
  %{?with_perl_bindings:-DENABLE_PERL=ON}        \
  %{?with_ruby_bindings:-DENABLE_RUBY=ON}        \
  -DENABLE_PYTHON=ON                             \
  -DPYTHON_EXECUTABLE=/usr/bin/python3.6         \
  -DPYTHON_LIBRARY=/usr/lib64/libpython3.6m.so   \
  -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m   \
  -DPython_ADDITIONAL_VERSIONS=3.6               \
  %{nil}
%ninja_build -C "%{_vpath_builddir}"
popd

%endif
%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%ninja_install -C "%{_vpath_builddir}"
%{?scl:EOF}

%if %{with python36}
pushd build-py36
%ninja_install -C "%{_vpath_builddir}"
popd
%endif

%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%ninja_test -C "%{_vpath_builddir}"
%{?scl:EOF}

%files
%license LICENSE*
%doc README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}ext.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}ext.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}ext.pc
# Own directory because we don't want to depend on cmake
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/%{name}*.3*

# Some small macro to list tools with mans
%global solv_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*

%files tools
%solv_tool deltainfoxml2solv
%solv_tool dumpsolv
%solv_tool installcheck
%solv_tool mergesolv
%solv_tool repomdxml2solv
%solv_tool rpmdb2solv
%solv_tool rpmmd2solv
%solv_tool rpms2solv
%solv_tool testsolv
%solv_tool updateinfoxml2solv
%solv_tool repo2solv
%if %{with comps}
  %solv_tool comps2solv
%endif
%if %{with appdata}
  %solv_tool appdata2solv
%endif
%if %{with debian_repo}
  %solv_tool deb2solv
%endif
%if %{with arch_repo}
  %solv_tool archpkgs2solv
  %solv_tool archrepo2solv
%endif
%if %{with helix_repo}
  %solv_tool helix2solv
%endif
%if %{with suse_repo}
  %solv_tool susetags2solv
%endif

%files demo
%solv_tool solv

%if %{with perl_bindings}
%files -n perl-%{libname}
%{perl_vendorarch}/%{libname}.pm
%{perl_vendorarch}/%{libname}.so
%endif

%if %{with ruby_bindings}
%files -n ruby-%{libname}
%{ruby_vendorarchdir}/%{libname}.so
%endif

%if %{with python2_bindings}
%files -n python2-%{libname}
%{python2_sitearch}/_%{libname}.so
%{python2_sitearch}/%{libname}.py*
%endif

%if %{with python3_bindings}
%files -n %{?scl_prefix}python%{python3_pkgversion}-%{libname}
%{python3_sitearch}/_%{libname}.so
%{python3_sitearch}/%{libname}.py
%if 0%{?!scl:1}
%{python3_sitearch}/__pycache__/%{libname}.*
%endif
%endif

%if %{with python36}
%files -n python3-%{libname}
/usr/lib64/python3.6/site-packages/_%{libname}.so
/usr/lib64/python3.6/site-packages/%{libname}.py
/usr/lib64/python3.6/site-packages/__pycache__/%{libname}.*
%endif

%changelog
* Wed Oct 27 2021 Evgeni Golov - 0.7.20-4
- Also build libsolv against Python 3.6 on EL8

* Tue Oct 26 2021 Evgeni Golov - 0.7.20-3
- Obsolete non-SCL Python 3 packages on EL7

* Tue Sep 28 2021 Evgeni Golov - 0.7.20-2
- Build against Python 3.8

* Tue Sep 28 2021 Evgeni Golov - 0.7.20-1
- Release libsolv 0.7.20

* Tue Mar 23 2021 Evgeni Golov - 0.7.17-1
- Release libsolv 0.7.17

* Tue Aug 18 2020 Evgeni Golov - 0.7.12-2
- Only build Python2 bindings on EL7

* Tue Apr 21 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.12-1
- Update to 0.7.12
