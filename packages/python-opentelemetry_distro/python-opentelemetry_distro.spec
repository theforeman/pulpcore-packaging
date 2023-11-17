%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_distro

Name:           python-%{pypi_name}
Version:        0.40b0
Release:        7%{?dist}
Summary:        OpenTelemetry Python Distro

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-distro
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
Requires:       python%{python3_pkgversion}-opentelemetry_api >= 1.12
Requires:       python%{python3_pkgversion}-opentelemetry_api < 2
Requires:       python%{python3_pkgversion}-opentelemetry_instrumentation == 0.40b0
Requires:       python%{python3_pkgversion}-opentelemetry_sdk >= 1.13
Requires:       python%{python3_pkgversion}-opentelemetry_sdk < 2

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}_otlp
Summary:        Metapackage for OpenTelemetry otlp extras
Version:        %{version}

Requires:       python%{python3_pkgversion}-%{pypi_name} = 0.40b0
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp = 1.19.0

Obsoletes:      python3-%{pypi_name}_otlp < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name}_otlp < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}_otlp
This is a metapackage bringing in “otlp” extras requires for
python3-opentelemetry-distro. It makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{pypi_name}_otlp
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info


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
%{python3_sitelib}/opentelemetry/distro
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-6
- Build against python 3.11

* Thu Aug 10 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-5
- Add otlp metapackage

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-4
- Change opentelemetry_instrumentation requirement from 0.40b0.dev to 0.40b0

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-3
- Update opentelemetry_instrumentation requirement

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-2
- Update opentelemetry dependency names

* Wed Jul 26 2023 Odilon Sousa - 0.40b0-1
- Initial package.
