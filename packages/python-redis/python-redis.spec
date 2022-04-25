%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name redis

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.5.3
Release:        3%{?dist}
Summary:        Python client for Redis key-value store

License:        MIT
URL:            https://github.com/andymccurdy/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.5.3-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.5.3-2
- Build against Python 3.8

* Thu Jun 04 2020 Evgeni Golov 3.5.3-1
- Update to 3.5.3

* Wed Mar 18 2020 Samir Jha 3.4.1-1
- Update to 3.4.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.1.0-1
- Initial package.
