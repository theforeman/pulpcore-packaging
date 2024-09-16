%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_api

Name:           python-%{pypi_name}
Version:        1.23.0
Release:        1%{?dist}
Summary:        OpenTelemetry Python API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-api/
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-deprecated >= 1.2.6
Requires:       python%{python3_pkgversion}-importlib-metadata >= 6.0
Requires:       python%{python3_pkgversion}-importlib-metadata < 7.0

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
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
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.23.0-1
- Update to 1.23.0

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-2
- Build against python 3.11

* Wed Jul 26 2023 Odilon Sousa - 1.19.0-1
- Initial package.
