%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-readonly-field

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.5
Release:        3%{?dist}
Summary:        Make Django model fields readonly

License:        MIT
URL:            https://github.com/peopledoc/django-readonly-field
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django >= 1.11
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 1.11
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
%{python3_sitelib}/django_readonly_field
%{python3_sitelib}/django_readonly_field-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Oct 26 2021 Evgeni Golov - 1.0.5-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 1.0.5-2
- Build against Python 3.8

* Thu Jul 30 2020 Samir Jha - 1.0.5-1
- Initial package.
