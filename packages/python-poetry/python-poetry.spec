%{?python_disable_dependency_generator}
%global pypi_name poetry

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Python dependency management and packaging made easy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-poetry/
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-build >= 0.10.0
Requires:       python%{python3_pkgversion}-build < 0.11.0
Requires:       python%{python3_pkgversion}-cachecontrol >= 0.12.9
Requires:       python%{python3_pkgversion}-cachecontrol < 0.13.0
Requires:       python%{python3_pkgversion}-cleo >= 2.0.0
Requires:       python%{python3_pkgversion}-cleo < 3.0.0
Requires:       python%{python3_pkgversion}-crashtest >= 0.4.1
Requires:       python%{python3_pkgversion}-crashtest < 0.5.0
Requires:       python%{python3_pkgversion}-dulwich >= 0.21.2
Requires:       python%{python3_pkgversion}-dulwich < 0.22.0
Requires:       python%{python3_pkgversion}-filelock >= 3.8.0
Requires:       python%{python3_pkgversion}-filelock < 4.0.0
Requires:       python%{python3_pkgversion}-html5lib >= 1.0
Requires:       python%{python3_pkgversion}-html5lib < 2.0
Requires:       python%{python3_pkgversion}-installer >= 0.7.0
Requires:       python%{python3_pkgversion}-installer < 0.8.0
Requires:       python%{python3_pkgversion}-jsonschema >= 4.10.0
Requires:       python%{python3_pkgversion}-jsonschema < 5.0.0
Requires:       python%{python3_pkgversion}-keyring >= 23.9.0
Requires:       python%{python3_pkgversion}-lockfile >= 0.12.2
Requires:       python%{python3_pkgversion}-packaging >= 20.4
Requires:       python%{python3_pkgversion}-pexpect >= 4.7.0
Requires:       python%{python3_pkgversion}-pkginfo >= 1.9.4
Requires:       python%{python3_pkgversion}-platformdirs >= 3.0.0
Requires:       python%{python3_pkgversion}-poetry_core >= 1.6.1
Requires:       python%{python3_pkgversion}-poetry_plugin_export >= 1.4.0
Requires:       python%{python3_pkgversion}-pyproject_hooks >= 1.0.0
Requires:       python%{python3_pkgversion}-requests-toolbelt >= 1.0.0
Requires:       python%{python3_pkgversion}-requests >= 2.18
Requires:       python%{python3_pkgversion}-requests < 3.0
Requires:       python%{python3_pkgversion}-shellingham >= 1.5.1
Requires:       python%{python3_pkgversion}-tomlkit >= 0.11.4
Requires:       python%{python3_pkgversion}-trove-classifiers >= 2022.5.19
Requires:       python%{python3_pkgversion}-urllib3 >= 1.26.0
Requires:       python%{python3_pkgversion}-virtualenv >= 20.22.0

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Mon Aug 07 2023 Odilon Sousa - 1.5.1-1
- Initial package.