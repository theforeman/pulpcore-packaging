%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name ecdsa

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.17.0
Release:        1%{?dist}
Summary:        ECDSA cryptographic signature library (pure python)

License:        MIT
URL:            http://github.com/tlsfuzzer/python-ecdsa
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gmpy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gmpy2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.9.0


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 19 2022 Yanis Guenane 0.17.0-1
- Update to 0.17.0

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 0.14.1-1
- Release python-ecdsa 0.14.1

* Mon Sep 06 2021 Evgeni Golov - 0.13.3-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.3-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 0.13.3-1
- Initial package.
