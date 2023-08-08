%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_instrumentation_django

Name:           python-%{pypi_name}
Version:        0.40b0
Release:        2%{?dist}
Summary:        OpenTelemetry Instrumentation for Django

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-django
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
Requires:  python%{python3_pkgversion}-opentelemetry_api >= 1.12
Requires:  python%{python3_pkgversion}-opentelemetry_api < 2
Requires:  python%{python3_pkgversion}-opentelemetry_instrumentation = 0.40b0
Requires:  python%{python3_pkgversion}-opentelemetry_instrumentation_wsgi = 0.40b0
Requires:  python%{python3_pkgversion}-opentelemetry_semantic_conventions = 0.40b0
Requires:  python%{python3_pkgversion}-opentelemetry_util_http = 0.40b0

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
%{python3_sitelib}/opentelemetry/instrumentation/django/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-2
- Update opentelemetry dependency names

* Wed Jul 26 2023 Odilon Sousa - 0.40b0-1
- Initial package.
