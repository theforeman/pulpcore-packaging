%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-automated-logging

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        6.1.3
Release:        1%{?dist}
Summary:        Django Database Based Automated Logging - finally solved and done in a proper way

License:        None
URL:            https://github.com/indietyp/django-automated-logging
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django < 4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-ipware < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-ipware >= 3.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-picklefield < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-picklefield >= 3.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-marshmallow < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-marshmallow >= 3.6.1


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
%doc README.md
%{python3_sitelib}/automated_logging
%{python3_sitelib}/django_automated_logging-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 20 2021 Odilon Sousa <osousa@redhat.com> - 6.1.3-1
- Release python-django-automated-logging 6.1.3

* Mon Sep 13 2021 Evgeni Golov - 6.1.1-1
- Initial package.
