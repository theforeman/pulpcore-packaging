%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-cloud-core
%global src_name google_cloud_core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Google Cloud API client core library

License:        Apache 2.0
URL:            https://github.com/googleapis/python-cloud-core
Source0:        https://files.pythonhosted.org/packages/source/g/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Conflicts:      python%{python3_pkgversion}-google-api-core = 2.3
Requires:       python%{python3_pkgversion}-google-api-core < 3
Requires:       python%{python3_pkgversion}-google-api-core >= 1.31.6
Requires:       python%{python3_pkgversion}-google-auth < 3
Requires:       python%{python3_pkgversion}-google-auth >= 1.25

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info



%build
set -ex
%pyproject_wheel



%install
set -ex
%pyproject_install



%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/google
%{python3_sitelib}/google_cloud_core-%{version}.dist-info/


%changelog
* Sun Apr 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.1-1
- Update to 2.5.1

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.0-1
- Update to 2.5.0

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.3-1
- Update to 2.4.3

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.4.2-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.2-1
- Update to 2.4.2

* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.4.1-1
- Initial package.
