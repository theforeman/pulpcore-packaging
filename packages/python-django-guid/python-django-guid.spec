%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-guid

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.2.1
Release:        1%{?dist}
Summary:        Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs

License:        None
URL:            https://github.com/snok/django-guid
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django < 5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 3.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 3.1.1


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
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
%doc docs/README_PYPI.rst
%{python3_sitelib}/django_guid
%{python3_sitelib}/django_guid-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 3.2.1-1
- Update to 3.2.1

* Tue Oct 19 2021 Evgeni Golov - 3.2.0-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 3.2.0-1
- Update to 3.2.0

* Wed Sep 08 2021 Evgeni Golov - 2.2.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Jan 18 2021 Evgeni Golov - 2.2.0-1
- Initial package.
