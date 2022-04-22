%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name toml

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.10.2
Release:        3%{?dist}
Summary:        Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://github.com/uiri/toml
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
* Fri Apr 22 2022 Yanis Guenane - 0.10.2-3
- Build against Python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.10.2-2
- Build against Python 3.8

* Mon Jun 28 2021 Evgeni Golov - 0.10.2-1
- Release python-toml 0.10.2

* Thu Jun 04 2020 Evgeni Golov 0.10.1-1
- Update to 0.10.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.10.0-1
- Initial package.
