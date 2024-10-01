%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_instrumentation

Name:           python-%{pypi_name}
Version:        0.48b0
Release:        1%{?dist}
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/opentelemetry-instrumentation/
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
Requires:       python%{python3_pkgversion}-opentelemetry_api >= 1.4
Requires:       python%{python3_pkgversion}-opentelemetry_api < 2
Requires:       python%{python3_pkgversion}-setuptools >= 16.0
Requires:       python%{python3_pkgversion}-wrapt >= 1.0.0
Requires:       python%{python3_pkgversion}-wrapt < 2.0.0

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
%{python3_sitelib}/opentelemetry/instrumentation
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/opentelemetry-bootstrap
%{_bindir}/opentelemetry-instrument

%changelog
* Tue Oct 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.48b0-1
- Update to 0.48b0

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.44b0-1
- Update to 0.44b0

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-5
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-4
- Build against python 3.11

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-3
- Update opentelemetry_api requirement

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 0.40b0-2
- Update opentelemetry dependency names

* Wed Jul 26 2023 Odilon Sousa - 0.40b0-1
- Initial package.
