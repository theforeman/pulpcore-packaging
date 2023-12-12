%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe
%global srcname markupsafe

# Our EL8 buildroots default to Python 3.8, but let's also build 3.6, just to be safe
# to make dnf happy
%if 0%{?rhel} == 8
%bcond_without python39
%else
%bcond_with python3
%endif

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.1.2
Release:        4%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}

%if %{with python36}
%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python36-devel
Provides:       python36-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
%{summary}
%endif

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}

%if %{with python36}
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
 /usr/bin/python3.6 setup.py  build --executable="/usr/bin/python3.6 -s"
%endif


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}

%if %{with python36}
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
 /usr/bin/python3.6 setup.py  install --skip-build --root %{buildroot}
%endif


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with python36}
%files -n python3-%{srcname}
/usr/lib64/python3.6/site-packages/markupsafe
/usr/lib64/python3.6/site-packages/%{pypi_name}-%{version}-py*.egg-info
%endif

%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2.1.2-1
- Update to 2.1.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.1-3
- Build against python 3.9

* Thu Jan 13 2022 Evgeni Golov - 2.0.1-2
- build markupsafe for Python 3.6 too

* Wed Nov 03 2021 Odilon Sousa 2.0.1-1
- Update to 2.0.1

* Mon Sep 06 2021 Evgeni Golov - 1.1.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.1-1
- Initial package.
