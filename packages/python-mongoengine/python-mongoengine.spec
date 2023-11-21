%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name mongoengine

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.20.0
Release:        5%{?dist}
Summary:        MongoEngine is a Python Object-Document Mapper for working with MongoDB

License:        MIT
URL:            http://mongoengine.org/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pymongo < 4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pymongo >= 3.4
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif



%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


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


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.20.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.20.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.20.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.20.0-2
- Build against Python 3.8

* Tue Sep 01 2020 Evgeni Golov 0.20.0-1
- Update to 0.20.0

* Tue Mar 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.19.1-3
- Bump pymongo requires

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.19.1-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 0.19.1-1
- Initial package.
