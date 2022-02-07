%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-import-export

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.7.1
Release:        1%{?dist}
Summary:        Django application and library for importing and exporting data with included admin integration

License:        BSD License
URL:            https://github.com/django-import-export/django-import-export
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Django >= 2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-diff-match-patch
Requires:       %{?scl_prefix}python%{python3_pkgversion}-tablib >= 3.0.0


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
%{python3_sitelib}/import_export
%{python3_sitelib}/django_import_export-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Feb 07 2022 Odilon Sousa 2.7.1-1
- Update to 2.7.1

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 2.6.1-1
- Release python-django-import-export 2.6.1

* Tue Oct 19 2021 Evgeni Golov - 2.5.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.5.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.5.0-1
- Update to 2.5.0

* Mon Nov 02 2020 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Tue Aug 25 2020 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Tue Apr 28 2020 Evgeni Golov - 2.0.2-1
- Initial package.
