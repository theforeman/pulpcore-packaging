%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-currentuser

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.5.3
Release:        3%{?dist}
Summary:        Conveniently store reference to request user on thread/db level

License:        BSD
URL:            https://github.com/PaesslerAG/django-currentuser
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django < 3.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 1.11.17
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
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_currentuser
%{python3_sitelib}/django_currentuser-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Oct 19 2021 Evgeni Golov - 0.5.3-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.5.3-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 0.5.3-1
- Update to 0.5.3

* Fri Mar 19 2021 Evgeni Golov 0.5.2-1
- Update to 0.5.2

* Tue Aug 25 2020 Evgeni Golov - 0.5.1-1
- Initial package.
