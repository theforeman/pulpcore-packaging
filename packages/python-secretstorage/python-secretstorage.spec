%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name SecretStorage
%global package_name secretstorage

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.5.0
Release:        2%{?dist}
Summary:        Python bindings to FreeDesktop.org Secret Service API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/mitya57/secretstorage
Source0:        https://files.pythonhosted.org/packages/source/s/%{package_name}/%{package_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-jeepney
Requires:       python%{python3_pkgversion}-cryptography

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{package_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 3.5.0-2
- Bump release for EL10 rebuild

* Sun Apr 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.0-1
- Update to 3.5.0
- Fix Source0: tarball filename uses lowercase (secretstorage) since 3.5.0

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 3.3.3-5
- Rebuild against python3.12

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.3.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.3.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.3-2
- Build against python 3.11

* Wed Jul 19 2023 Odilon Sousa - 3.3.3-1
- Initial package.