%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name six

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.16.0
Release:        2%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 1.16.0-2
- Rebuild against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 1.16.0-1
- Release python-six 1.16.0

* Mon Sep 06 2021 Evgeni Golov - 1.15.0-2
- Build against Python 3.8

* Thu Jun 04 2020 Evgeni Golov 1.15.0-1
- Update to 1.15.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.14.0-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 1.14.0-1
- Update to 1.14.0

* Mon Nov 18 2019 Evgeni Golov - 1.13.0-1
- Initial package.
