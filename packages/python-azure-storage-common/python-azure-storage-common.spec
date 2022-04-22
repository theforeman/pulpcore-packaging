%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name azure-storage-common

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.1.0
Release:        3%{?dist}
Summary:        Microsoft Azure Storage Common Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-storage-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-azure-common >= 1.1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dateutil
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests


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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_storage_common-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.1.0-3
- Build against python 3.9

* Wed Oct 27 2021 Evgeni Golov - 2.1.0-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 2.1.0-1
- Initial package.
