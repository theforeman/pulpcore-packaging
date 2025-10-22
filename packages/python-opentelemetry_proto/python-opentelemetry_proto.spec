%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name opentelemetry_proto

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.36.0
Release:        1%{?dist}
Summary:        OpenTelemetry Python Proto.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-proto/
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:       python%{python3_pkgversion}-protobuf >= 5
Requires:       python%{python3_pkgversion}-protobuf < 6

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/opentelemetry/proto
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.0-1
- Update to 1.36.0

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.30.0-1
- Update to 1.30.0

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 1.27.0-3
- Add obsoletes for python3.11 package

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 1.27.0-2
- Rebuild against python3.12

* Tue Oct 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.27.0-1
- Update to 1.27.0

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.23.0-1
- Update to 1.23.0

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-4
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-3
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-2
- Update opentelemetry dependency names

* Wed Jul 26 2023 Odilon Sousa - 1.19.0-1
- Initial package.
