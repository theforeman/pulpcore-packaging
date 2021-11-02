%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name azure-storage-blob

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        12.9.0
Release:        1%{?dist}
Summary:        Microsoft Azure Blob Storage Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-azure-core < 2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-azure-core >= 1.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 2.1.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-msrest >= 0.6.21

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
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_storage_blob-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 02 2021 Evgeni Golov - 12.9.0-1
- Update to 12.9.0

* Wed Oct 27 2021 Evgeni Golov - 2.1.0-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 2.1.0-1
- Initial package.
