%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-api-core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.30.2
Release:        1%{?dist}
Summary:        Google API client core library

License:        Apache 2.0
URL:            https://github.com/googleapis/python-api-core
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_api_core-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


Conflicts:      python%{python3_pkgversion}-protobuf = 3.20
Conflicts:      python%{python3_pkgversion}-protobuf = 3.20.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.2
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.3
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.4
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.5
Requires:       python%{python3_pkgversion}-google-auth < 3
Requires:       python%{python3_pkgversion}-google-auth >= 2.14.1
Requires:       python%{python3_pkgversion}-googleapis-common-protos < 2
Requires:       python%{python3_pkgversion}-googleapis-common-protos >= 1.56.2
Requires:       python%{python3_pkgversion}-proto-plus < 2
Requires:       python%{python3_pkgversion}-proto-plus >= 1.22.3
Requires:       python%{python3_pkgversion}-protobuf < 6
Requires:       python%{python3_pkgversion}-protobuf >= 3.19.5
Requires:       python%{python3_pkgversion}-requests < 3
Requires:       python%{python3_pkgversion}-requests >= 2.18

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n google_api_core-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
set -ex
%py3_build



%install
set -ex
%py3_install



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/google_api_core-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Apr 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.30.2-1
- Update to 2.30.2

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.30.0-1
- Update to 2.30.0

* Sun Jun 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.25.1-1
- Update to 2.25.1

* Wed Jun 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.25.0-1
- Update to 2.25.0

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.2-1
- Update to 2.24.2

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.24.1-2
- Rebuild against python3.12

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.1-1
- Update to 2.24.1

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.0-1
- Update to 2.24.0

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.23.0-1
- Update to 2.23.0

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.22.0-1
- Update to 2.22.0

* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.21.0-1
- Update to 2.21.0

* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.20.0-1
- Initial package.
