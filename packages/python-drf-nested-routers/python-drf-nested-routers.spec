%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name drf-nested-routers

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.93.4
Release:        4%{?dist}
Summary:        Nested resources for the Django Rest Framework

License:        Apache
URL:            https://github.com/alanjds/drf-nested-routers
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 1.11
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.6.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif


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
%doc README.md README.rst
%{python3_sitelib}/rest_framework_nested
%{python3_sitelib}/rest_framework_nested/runtests
%{python3_sitelib}/drf_nested_routers-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.93.4-4
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.93.4-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.93.4-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 0.93.4-1
- Release python-drf-nested-routers 0.93.4

* Tue Oct 19 2021 Evgeni Golov - 0.93.3-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.93.3-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.93.3-1
- Update to 0.93.3

* Mon Nov 02 2020 Evgeni Golov 0.92.1-1
- Update to 0.92.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.91-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.91-1
- Initial package.
