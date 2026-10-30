%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name opentelemetry_exporter_http_transport

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.66b2
Release:        1%{?dist}
Summary:        OpenTelemetry Exporters HTTP transport

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-http-transport
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-opentelemetry_api >= 1.15
Requires:       python%{python3_pkgversion}-opentelemetry_api < 2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}

%package -n python%{python3_pkgversion}-%{pypi_name}+requests
Summary:        Requests transport extra for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-requests >= 2.25
Requires:       python%{python3_pkgversion}-requests < 3

%description -n python%{python3_pkgversion}-%{pypi_name}+requests
This metapackage installs the requests backend dependency for %{name}.

%files -n python%{python3_pkgversion}-%{pypi_name}+requests
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%package -n python%{python3_pkgversion}-%{pypi_name}+urllib3
Summary:        urllib3 transport extra for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-urllib3 >= 1.26

%description -n python%{python3_pkgversion}-%{pypi_name}+urllib3
This metapackage installs the urllib3 backend dependency for %{name}.

%files -n python%{python3_pkgversion}-%{pypi_name}+urllib3
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
%{python3_sitelib}/opentelemetry/exporter/http/transport/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Oct 30 2026 Odilon Sousa <osousa@redhat.com> - 0.66b2-1
- Initial package.
