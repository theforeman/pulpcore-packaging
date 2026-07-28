%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.7
%global pypi_name azure-core
%global src_name azure_core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.41.0
Release:        2%{?dist}
Summary:        Microsoft Azure Core Library for Python

License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-requests >= 2.21.0
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.6.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 1.41.0-2
- Bump release for EL10 rebuild

* Sun May 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.41.0-1
- Update to 1.41.0

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.40.0-1
- Update to 1.40.0

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.39.0-1
- Update to 1.39.0
- Switch to pyproject build (setup.py removed upstream)
- Drop stale Requires: python-six (removed from upstream deps since 1.35.0)
- Fix License tag to SPDX identifier
- Fix PEP 639 license field in pyproject.toml for RHEL 9 setuptools

* Wed Jul 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.0-1
- Update to 1.35.0

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.34.0-1
- Update to 1.34.0

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 1.32.0-2
- Rebuild against python3.12

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.32.0-1
- Update to 1.32.0

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
