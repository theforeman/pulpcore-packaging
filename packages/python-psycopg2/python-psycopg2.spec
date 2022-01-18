%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg2

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.9.3
Release:        1%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

License:        LGPL with exceptions
URL:            https://psycopg.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%license LICENSE doc/src/license.rst doc/COPYING.LESSER
%doc README.rst doc/README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 2.9.3-1
- Update to 2.9.3

* Wed Sep 08 2021 Evgeni Golov 2.9.1-1
- Update to 2.9.1

* Mon Sep 06 2021 Evgeni Golov - 2.8.6-2
- Build against Python 3.8

* Mon Sep 07 2020 Evgeni Golov 2.8.6-1
- Update to 2.8.6

* Tue Apr 14 2020 Evgeni Golov 2.8.5-1
- Update to 2.8.5

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.8.4-1
- Initial package.
