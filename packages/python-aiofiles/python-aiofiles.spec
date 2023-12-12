%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name aiofiles

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        22.1.0
Release:        4%{?dist}
Summary:        File support for asyncio

License:        Apache 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 22.1.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 22.1.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 22.1.0-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 22.1.0-1
- Update to 22.1.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.8.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 0.8.0-1
- Release python-aiofiles 0.8.0

* Mon Sep 06 2021 Evgeni Golov - 0.7.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Thu Oct 29 2020 Evgeni Golov 0.6.0-1
- Update to 0.6.0

* Tue Apr 14 2020 Evgeni Golov 0.5.0-1
- Update to 0.5.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.4.0-1
- Initial package.
