%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

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

# Always build Python3 bindings
%bcond_without python3

# Our EL8 buildroots default to Python 3.8, but we also need a 3.6 build of libcomps
# to make dnf happy
%if 0%{?rhel} == 8
%bcond_without python36
%else
%bcond_with python36
%endif

# Our EL9 buildroots default to Python 3.9, we also need a 3.9 build of libcomps
# to make dnf happy
%if 0%{?rhel} == 9
%bcond_without python39
%else
%bcond_with python39
%endif

# Never build docs by default
%bcond_with doc

Name:           libcomps
Version:        0.1.18
Release:        7%{?dist}
Summary:        Comps XML file manipulation library

License:        GPLv2+
URL:            https://github.com/rpm-software-management/libcomps
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  check-devel
BuildRequires:  expat-devel
BuildRequires:  zlib-devel

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package devel
Summary:        Development files for libcomps library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libcomps library.

%if %{with doc}
%package doc
Summary:        Documentation files for libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Documentation files for libcomps library.

%package -n %{?scl_prefix}python-%{name}-doc
Summary:        Documentation files for python bindings libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-sphinx

%description -n %{?scl_prefix}python-%{name}-doc
Documentation files for python bindings libcomps library.
%endif

%if %{with python3}
%package -n %{?scl_prefix}python%{python3_pkgversion}-%{name}
Summary:        Python 3 bindings for libcomps library
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{?scl_prefix}platform-python-%{name} < %{version}-%{release}
%if 0%{?scl:1}
Obsoletes:      python3-%{name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{name} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{name}
Python3 bindings for libcomps library.
%endif

%if %{with python36}
%package -n python3-%{name}
Summary:        Python 3 bindings for libcomps library
BuildRequires:  python36-devel
Provides:       python36-%{name} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      platform-python-%{name} < %{version}-%{release}

%description -n python3-%{name}
Python3 bindings for libcomps library.
%endif

%if %{with python39}
%package -n python3-%{name}
Summary:        Python 3 bindings for libcomps library
BuildRequires:  python3-devel
Provides:       python3-%{name} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      platform-python-%{name} < %{version}-%{release}

%description -n python3-%{name}
Python3 bindings for libcomps library.
%endif

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{name}-%{version}
# workaround for https://github.com/rpm-software-management/libcomps/pull/64
sed -i 's/EXACT//' libcomps/src/python/src/CMakeLists.txt

# it can't detect our special PYTHONPATH and uses the compiled-in from the SCL Python
%if 0%{?scl:1}
sed -i "/OUTPUT_VARIABLE PYTHON_INSTALL_DIR/ s#))#).replace('rh/rh-python38', 'theforeman/tfm-pulpcore'))#" libcomps/src/python/src/CMakeLists.txt
%endif

%if %{with python3}
mkdir build-py3
%endif
%if %{with python36}
mkdir build-py36
%endif
%if %{with python39}
mkdir build-py39
%endif
%if %{with doc}
mkdir build-doc
%endif
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex

%if %{with python3}
%if 0%{?rhel} == 7
pushd build-py3
  # explicitly set INCLUDE_DIR and LIBRARY when inside the SCL, otherwise it's not found
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3 -DPYTHON_EXECUTABLE=%{__python3} %{?scl:-DPYTHON_INCLUDE_DIR=/opt/rh/rh-python38/root/usr/include/python3.8/ -DPYTHON_LIBRARY=/opt/rh/rh-python38/root/lib64/libpython3.8.so}
  %make_build
popd
%else
pushd build-py3
  # Build for el9
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3 -DPYTHON_EXECUTABLE=%{__python3}
  %cmake_build
popd
%endif
%endif

%if %{with python36}
pushd build-py36
  # explicitly set INCLUDE_DIR and LIBRARY when inside the SCL, otherwise it's not found
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3.6 -DPYTHON_EXECUTABLE=/usr/bin/python3.6
  %make_build
popd
%endif

%if %{with python39}
pushd build-py39
  # explicitly set INCLUDE_DIR and LIBRARY when inside the SCL, otherwise it's not found
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3.9 -DPYTHON_EXECUTABLE=/usr/bin/python3.9
  %cmake_build
popd
%endif

%if %{with doc}
pushd build-doc
%if %{with python3}
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3
%endif
  make %{?_smp_mflags} docs
  make %{?_smp_mflags} pydocs
popd
%endif
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex

%if %{with python3}
pushd build-py3
%if 0%{?rhel} == 7
  %make_install
%else
  %cmake_install
%endif
popd
%endif

%if %{with python36}
pushd build-py36
  %make_install
popd
%endif

%if %{with python39}
pushd build-py39
  %cmake_install
popd
%endif
%{?scl:EOF}

%if 0%{?rhel} != 9
%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# only run tests on python3 as they are broken on py2/EL7

%if %{with python3}
pushd build-py3
  make test
  make pytest
%endif
popd
%endif

%{?scl:EOF}

%if %{undefined ldconfig_scriptlets}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%else
%ldconfig_scriptlets
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%if %{with doc}
%files doc
%doc build-doc/docs/libcomps-doc/html

%files -n %{?scl_prefix}python-%{name}-doc
%doc build-doc/src/python/docs/html
%endif

%if %{with python3}
%files -n %{?scl_prefix}python%{python3_pkgversion}-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info
%endif

%if %{with python36}
%files -n python3-%{name}
/usr/lib64/python3.6/site-packages/%{name}/
/usr/lib64/python3.6/site-packages/%{name}-%{version}-py*.egg-info
%endif

%if %{with python39}
%files -n python3-%{name}
/usr/lib64/python3.9/site-packages/%{name}/
/usr/lib64/python3.9/site-packages/%{name}-%{version}-py*.egg-info
%endif

%changelog
* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 0.1.18-7
- Build python3.9 bits on EL9

* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 0.1.18-6
- Add egg again for python-3.11 builds

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.1.18-5
- Build against python 3.11

* Thu May 12 2022 Yanis Guenane <yguenane@redhat.com> - 0.1.18-4
- Fix obsolete named package

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.1.18-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 0.1.18-2
- Rebuilding Against python 3.9

* Mon Nov 22 2021 Evgeni Golov - 0.1.18-1
- Release libcomps 0.1.18

* Tue Oct 26 2021 Evgeni Golov - 0.1.15-4
- Obsolete non-SCL Python 3 packages on EL7

* Wed Oct 13 2021 Evgeni Golov - 0.1.15-3
- Also build libcomps against Python 3.6 on EL8

* Tue Sep 14 2021 Evgeni Golov - 0.1.15-2
- Build against Python 3.8

* Wed Apr 01 2020 Ales Matej <amatej@redhat.com> - 0.1.15-1
- Update to 0.1.15
- Do not skip type=mandatory in xml output (RhBug:1771224)

* Fri Jan 31 2020 Ales Matej <amatej@redhat.com> - 0.1.14-4
- Fix global header variable defined without extern for gcc-10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.1.14-2
- Fix inline vs static inline issue for gcc-10

* Fri Nov 29 2019 Ales Matej <amatej@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Fri Nov 29 2019 Ales Matej <amatej@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.11-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.11-4
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.11-3
- Fix Python method descriptors for Python 3.8 (#1734777)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Wed Feb 13 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Marek Blaha <mblaha@redhat.com> - 0.1.8-15
- Disable Python 2 bindings for Fedora >= 30

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-13
- Rebuilt for Python 3.7

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.8-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-10
- Switch to %%ldconfig_scriptlets

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-9
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-8
- Remove platform-python subpackage

* Fri Sep 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-7
- Disable platform python on old releases

* Thu Aug 10 2017 Lumír Balhar <lbalhar@redhat.com> - 0.1.8-6
- Add Platform Python subpackage (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.1.8-2
- Rebuild for Python 3.6

* Thu Sep 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Tue Aug 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.7-6
- Add %%{?system_python_abi}

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.7-4
- Adopt to new packaging guidelines
- Use %%license macro
- Fix file ownerships

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 0.1.7-2
- Rebuilt for Python3.5 rebuild

* Thu Jul 02 2015 Jindrich Luza <jluza@redhat.com> 0.1.7
- added langpacks to union process
- comps DOCTYPE read-write-read fix
- support biarchonly attribute
- fixed rhbz#1073885 rhbz#1073890 rhbz#1073907 rhbz#1073979
- fix rhbz#1073079
- comps_*_match() now support fnmatching
- added libpycomps.MATCH_IGNORECASE as matching flag
- added group.packages_match
- added comps.groups_match, comps.categories_match, comps.entironments_match
- PyCOMPS_Package hash
- cmake-2.6, python-2.6, RHEL-6 compatible
- '_arch' attribute change to 'arch'
- empty 'arch' attribute will be ommited from output from now

* Wed Jan 29 2014 Jindrich Luza <jluza@redhat.com> 0.1.6
- version bumped
- added libcomps.MDict.keys()
-         libcomps.MDict.values()
-         libcomps.MDict.items()
-         libcomps.MDict.clear()
-         libcomps.MDict.update()
-         libcomps.MDict.copy()
- COMPS_List replaced with COMPS_HSList
- added missing basearchonly to DocGroupPackage
- python3/CMakeLists.txt fixed
- added explicit attributes support for xml options
- added arch_filter test for python
- insert method in libcomps.Sequence
- Unioning is now accomplished with replace x append policy
- Weaker package equality check (comparing only name now)
- Fixed leeks in unioning
- modified test_merge_comps test_libcomps
- dictionaries are now storing keys in alphabetical order
- comps parser redesigned
- change python/tests directory composition
- added elem attributes check in parser
- xml output '_arch' attribute support
- parser and xml output defaults options for specify defaults values
- comps object validation in python
- added validity checker before append/set object to list (python only)
- .validate() method
- added libcomps.Dict.keys
-         libcomps.Dict.values
-         libcomps.Dict.items
-         libcomps.Dict.clear
-         libcomps.Dict.update
-         libcomps.Dict.copy
- added xml output options (comps.xml_str([options = {}]), comps.xml_f(options = {}))

* Wed Oct 23 2013 Jindrich Luza <jluza@redhat.com> 0.1.4-4
- group.uservisible is true by default now.
- fixed comps_mobjradix parent node problem
- implemented bindings for blacklist, whiteout and langpacks
- COMPS_Logger redesigned

* Tue Oct 08 2013 Jindrich Luza <jluza@redhat.com> 0.1.5
- version bump
- PyCOMPS_Sequence.__getitem__["objectid"] implemented for libcomps.GroupList, libcomps.CategoryList, libcomps.EnvList
- added missing files
- missing display_order fix for libcomps.Environment

* Tue Oct 01 2013 Jindrich Luza <jluza@redhat.com> 0.1.4
- added missing files
- architectural redesign finished
- fixed #1003986 by Gustavo Luiz Duarte guidelines (but not tested on ppc)
- fixed bug #1000449
- fixed bug #1000442
- added GroupId.default test
- some minor unreported bugs discovered during testing fixed
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log
- version bumped. Python bindings is now easier.
- added missing files

* Tue Aug 20 2013 Jindrich Luza <jluza@redhat.com> 0.1.3
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log

* Thu Jul 18 2013 Jindrich Luza <jluza@redhat.com> 0.1.2
- automatic changelog system
- fixed issue #14
- libcomps.Dict is now behave more like python dict. Implemented iter(libcomps.Dict)
- libcomps.iteritems() and libcomps.itervalues()
- remaked error reporting system.
-     libcomps.Comps.fromxml_f and libcomps.Comps.fromxml_str now return
-     -1, 0 or 1. 0 means parse procedure completed without any problem,
-     1 means there's some errors or warnings but not fatal. -1 indicates
-     fatal error problem (some results maybe given, but probably incomplete
-     and invalid)
- errors catched during parsing can be obtained by calling
-     libcomps.Comps.get_last_parse_errors
- all log is given by
-     libcomps.Comps.get_last_parse_log
- prop system complete
- fixed issue 1
- fixed issue 3
- added <packagereq requires=...> support
- new prop system in progress....
- separated doc package
- some minor fixes in CMakeFiles
- improved integrated tests

* Tue Jun 25 2013 Jindrich Luza <jluza@redhat.com> 0.1.1-1
- Automatic commit of package [libcomps] release [0.1.1-1].

