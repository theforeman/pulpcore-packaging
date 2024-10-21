%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name azure-core
%global src_name azure_core

Name:           python-%{pypi_name}
Version:        1.31.0
Release:        1%{?dist}
Summary:        Microsoft Azure Core Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-requests >= 2.21.0
Requires:       python%{python3_pkgversion}-six >= 1.11
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.6.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_core-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.31.0-1
- Update to 1.31.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.19.1-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.19.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.19.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.19.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.19.1-2
- Build against python 3.9

* Tue Nov 02 2021 Evgeni Golov - 1.19.1-1
- Initial package.
