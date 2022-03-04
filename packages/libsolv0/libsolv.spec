%global libname solv

%bcond_with python2_bindings
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with perl_bindings
%bcond_with ruby_bindings
%bcond_with python3_bindings
%else
%bcond_without perl_bindings
%bcond_without ruby_bindings
%bcond_without python3_bindings
%endif
# Creates special prefixed pseudo-packages from appdata metadata
%bcond_with appdata
# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
# For rich dependencies
%bcond_without complex_deps
%if 0%{?rhel}
%bcond_with helix_repo
%bcond_with suse_repo
%bcond_with debian_repo
%bcond_with arch_repo
# For handling deb + rpm at the same time
%bcond_with multi_semantics
%else
%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo
# For handling deb + rpm at the same time
%bcond_without multi_semantics
%endif

Name:           lib%{libname}0
Version:        0.6.34
Release:        4%{?dist}
Summary:        Package dependency solver

License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source0:        %{url}/archive/%{version}/lib%{libname}-%{version}.tar.gz
Patch0001:      0001-Make-sure-that-targeted-updates-dont-do-reinstalls.patch
Patch0002:      0002-Fix-testsolv-segfault.patch
Patch0003:      0003-Fix-testsolv-segfaults.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel
BuildRequires:  expat-devel
# -DFEDORA=1
# -DENABLE_RPMDB=ON
BuildRequires:  libdb-devel
# -DENABLE_LZMA_COMPRESSION=ON
BuildRequires:  xz-devel
# -DENABLE_BZIP2_COMPRESSION=ON
BuildRequires:  bzip2-devel

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
Obsoletes:      %{name}-test < 0.6.11-2
# repo2solv dependencies. All of those are used in shell-script.
Requires:       %{_bindir}/gzip
Requires:       %{_bindir}/bzip2
Requires:       %{_bindir}/lzma
Requires:       %{_bindir}/xz
Requires:       %{_bindir}/cat
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
%package -n python3-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python3-%{libname}}
BuildRequires:  swig
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%prep
%autosetup -p1 -n lib%{libname}-%{version}

%build
%cmake . -Bbuild                                \
  -DFEDORA=1                                    \
  -DENABLE_RPMDB=ON                             \
  -DENABLE_RPMDB_BYRPMHEADER=ON                 \
  -DENABLE_RPMDB_LIBRPM=OFF                     \
  -DENABLE_RPMPKG_LIBRPM=OFF                    \
  -DENABLE_RPMMD=ON                             \
  %{?with_comps:-DENABLE_COMPS=ON}              \
  %{?with_appdata:-DENABLE_APPDATA=ON}          \
  -DUSE_VENDORDIRS=ON                           \
  -DWITH_LIBXML2=OFF                            \
  -DENABLE_LZMA_COMPRESSION=ON                  \
  -DENABLE_BZIP2_COMPRESSION=ON                 \
  %{?with_helix_repo:-DENABLE_HELIXREPO=ON}     \
  %{?with_suse_repo:-DENABLE_SUSEREPO=ON}       \
  %{?with_debian_repo:-DENABLE_DEBIAN=ON}       \
  %{?with_arch_repo:-DENABLE_ARCHREPO=ON}       \
  %{?with_multi_semantics:-DMULTI_SEMANTICS=ON} \
  %{?with_complex_deps:-DENABLE_COMPLEX_DEPS=1} \
  %{?with_perl_bindings:-DENABLE_PERL=ON}       \
  %{?with_ruby_bindings:-DENABLE_RUBY=ON}       \
  %{?with_python2_bindings:-DENABLE_PYTHON=ON}  \
  %{?with_python3_bindings:-DENABLE_PYTHON3=ON} \
  %{nil}
%make_build -C build

%install
%make_install -C build

mv %{buildroot}%{_bindir}/repo2solv{.sh,}

%check
%make_build test -C build

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE*
%doc README
%{_libdir}/lib%{libname}.so.*
%{_libdir}/lib%{libname}ext.so.*

%files devel
%{_libdir}/lib%{libname}.so
%{_libdir}/lib%{libname}ext.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/lib%{libname}.pc
%{_libdir}/pkgconfig/lib%{libname}ext.pc
# Own directory because we don't want to depend on cmake
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/lib%{libname}*.3*

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

%{_bindir}/repo2solv

%files demo
%{_bindir}/solv

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
%files -n python3-%{libname}
%{python3_sitearch}/_%{libname}.so
%{python3_sitearch}/%{libname}.py
%{python3_sitearch}/__pycache__/%{libname}.*
%endif

%changelog
* Wed Mar 27 2019 Michal Domonkos <mdomonko@redhat.com> - 0.6.34-4
- Polish the changelog

* Thu Mar 21 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.6.34-3
- Make sure that targeted updates don't do reinstalls
- Resolves: bug#1668256
- Fix NULL pointer dereference (CVE-2018-20532, CVE-2018-20533)
- Resolves: bug#1669562
- Resolves: bug#1669576
- Fix illegal address access in pool_whatprovides (CVE-2018-20534)
- Resolves: bug#1670453

* Wed Jun 20 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.6.34-2
- Add changelog

* Wed Jun 20 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.6.34-1
- Update to 0.6.34

* Fri Sep 22 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.26-2
- Enable python bindings

* Sun Feb 19 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.26-1
- Update to 0.6.26

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.25-1
- Update to 0.6.25

* Fri Nov 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.24-1
- Update to 0.6.24

* Tue Jul 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.20-5
- Make obsoletes non-architecture dependent (RHBZ #1354479)

* Tue May 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.20-4
- Properly obsolete -test subpkg

* Mon May 30 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.20-3
- Rebase to 0.6.20 with 2 critical patches (RHBZ #1334401)

* Wed Jun 3 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-1
- initial package for RHEL 7.2 without unnecessary bindings
