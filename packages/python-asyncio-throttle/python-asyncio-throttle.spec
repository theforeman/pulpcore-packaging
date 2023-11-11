%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name asyncio-throttle

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.2
Release:        4%{?dist}
Summary:        Simple, easy-to-use throttler for asyncio

License:        MIT
URL:            https://github.com/hallazzang/asyncio-throttle
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
%doc README.md
%{python3_sitelib}/asyncio_throttle
%{python3_sitelib}/asyncio_throttle-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.2-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.2-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.2-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 1.0.2-1
- Update to 1.0.2

* Fri Mar 19 2021 Evgeni Golov - 1.0.1-1
- Initial package.
