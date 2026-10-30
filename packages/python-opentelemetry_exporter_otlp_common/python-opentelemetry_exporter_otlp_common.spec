%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name opentelemetry_exporter_otlp_common

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.66b2
Release:        1%{?dist}
Summary:        OpenTelemetry OTLP HTTP export utilities

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-common
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-opentelemetry_sdk >= 1.45.2
Requires:       python%{python3_pkgversion}-opentelemetry_sdk < 1.46

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}

%package -n python%{python3_pkgversion}-%{pypi_name}+http
Summary:        HTTP extra for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_http_transport = 0.66b2

%description -n python%{python3_pkgversion}-%{pypi_name}+http
This metapackage installs the HTTP transport dependency for %{name}.

%files -n python%{python3_pkgversion}-%{pypi_name}+http
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

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
%license LICENSE
%doc README.rst
%{python3_sitelib}/opentelemetry/exporter/otlp/common/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Oct 30 2026 Odilon Sousa <osousa@redhat.com> - 0.66b2-1
- Initial package.
