%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name anyio

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.14.2
Release:        1%{?dist}
Summary:        High level compatibility layer for multiple asynchronous event loop implementations

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/anyio/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-idna >= 2.8
Requires:       python%{python3_pkgversion}-sniffio >= 1.1
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.5

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = \"\(.*\)\"/license = {text = \"\1\"}/' pyproject.toml
# Remove bundled egg-info
# rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sun Aug 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.14.2-1
- Update to 4.14.2

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 4.14.1-2
- Bump release for EL10 rebuild

* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.14.1-1
- Update to 4.14.1

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.13.0-1
- Update to 4.13.0
- Fix PEP 639 license field for RHEL 9 pip compatibility

* Wed Apr 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.9.0-1
- Update to 4.9.0

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 4.8.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.8.0-1
- Update to 4.8.0

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.6.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.6.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.6.2-2
- Build against python 3.11

* Fri Jul 21 2023 Odilon Sousa - 3.6.2-1
- Initial package.