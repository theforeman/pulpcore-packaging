%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name azure-storage-common

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        7%{?dist}
Summary:        Microsoft Azure Storage Common Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-storage-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-azure-common >= 1.1.5
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-requests


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_storage_common-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.0-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.1.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.1.0-3
- Build against python 3.9

* Wed Oct 27 2021 Evgeni Golov - 2.1.0-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 2.1.0-1
- Initial package.
