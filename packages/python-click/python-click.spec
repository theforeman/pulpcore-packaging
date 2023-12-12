%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name click

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        8.1.3
Release:        4%{?dist}
Summary:        Composable command line interface toolkit

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/click/
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 8.1.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 8.1.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 8.1.3-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 8.1.3-1
- Update to 8.1.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 8.0.3-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 8.0.3-1
- Update to 8.0.3

* Wed Sep 08 2021 Evgeni Golov 8.0.1-1
- Update to 8.0.1

* Mon Sep 06 2021 Evgeni Golov - 7.1.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 7.1.2-1
- Update to 7.1.2

* Wed Mar 18 2020 Samir Jha 7.1.1-1
- Update to 7.1.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 7.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 7.0-1
- Initial package.
