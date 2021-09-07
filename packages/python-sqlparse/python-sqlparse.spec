%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name sqlparse

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        A non-validating SQL parser

License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%license LICENSE docs/source/license.rst
%doc README.rst
%{_bindir}/sqlformat
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 0.4.1-2
- Build against Python 3.8

* Thu Oct 29 2020 Evgeni Golov 0.4.1-1
- Update to 0.4.1

* Wed Mar 18 2020 Samir Jha 0.3.1-1
- Update to 0.3.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.3.0-1
- Initial package.
