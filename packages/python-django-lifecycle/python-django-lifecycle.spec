%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-lifecycle

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        Declarative model lifecycle hooks

License:        MIT
URL:            https://github.com/rsinger86/django-lifecycle
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urlman >= 1.2.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/django_lifecycle
%{python3_sitelib}/django_lifecycle-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.9.3-1
- Release python-django-lifecycle 0.9.3

* Tue Oct 19 2021 Evgeni Golov - 0.9.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.9.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.9.1-1
- Update to 0.9.1

* Fri Oct 23 2020 Evgeni Golov - 0.8.0-1
- Release python-django-lifecycle 0.8.0

* Tue Aug 25 2020 Evgeni Golov - 0.7.7-1
- Initial package.
