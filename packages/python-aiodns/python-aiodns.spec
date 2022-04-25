%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name aiodns

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.0.0
Release:        3%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pycares >= 4.0.0


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
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.0.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Nov 05 2020 Evgeni Golov - 2.0.0-3
- Fix License tag in spec file

* Wed Apr 01 2020 Evgeni Golov - 2.0.0-2
- Add python%{python3_pkgversion}-typing to Requires

* Wed Mar 18 2020 Samir Jha - 2.0.0-1
- Initial package.
