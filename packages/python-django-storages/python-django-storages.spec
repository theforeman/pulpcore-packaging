%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-storages

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.11.1
Release:        1%{?dist}
Summary:        Support for many storage backends in Django

License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-azure-storage-blob < 12.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-azure-storage-blob >= 1.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-boto3 >= 1.4.4


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
%{python3_sitelib}/storages
%{python3_sitelib}/django_storages-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Sep 03 2021 Evgeni Golov - 1.11.1-1
- Initial package.
