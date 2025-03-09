%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name poetry

Name:           python-%{pypi_name}
Version:        2.1.1
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
Requires:       python%{python3_pkgversion}-build >= 1.2.1
Requires:       python%{python3_pkgversion}-cachecontrol >= 0.14.0
Requires:       python%{python3_pkgversion}-cleo >= 2.1.0
Requires:       python%{python3_pkgversion}-crashtest >= 0.4.1
Requires:       python%{python3_pkgversion}-crashtest < 0.5.0
Requires:       python%{python3_pkgversion}-dulwich >= 0.22.6
Requires:       python%{python3_pkgversion}-dulwich < 0.23.0
Requires:       python%{python3_pkgversion}-fastjsonschema >= 2.18.0
Requires:       python%{python3_pkgversion}-filelock >= 3.8.0
Requires:       python%{python3_pkgversion}-filelock < 4.0.0
Requires:       python%{python3_pkgversion}-html5lib >= 1.0
Requires:       python%{python3_pkgversion}-html5lib < 2.0
Requires:       python%{python3_pkgversion}-installer >= 0.7.0
Requires:       python%{python3_pkgversion}-installer < 0.8.0
Requires:       python%{python3_pkgversion}-jsonschema >= 4.10.0
Requires:       python%{python3_pkgversion}-jsonschema < 5.0.0
Requires:       python%{python3_pkgversion}-keyring >= 24.0.0
Requires:       python%{python3_pkgversion}-lockfile >= 0.12.2
Requires:       python%{python3_pkgversion}-packaging >= 24.0
Requires:       python%{python3_pkgversion}-pexpect >= 4.7.0
Requires:       python%{python3_pkgversion}-pkginfo >= 1.12
Requires:       python%{python3_pkgversion}-platformdirs >= 3.0.0
Requires:       python%{python3_pkgversion}-platformdirs < 5
Requires:       python%{python3_pkgversion}-poetry_core == %{version}
Requires:       python%{python3_pkgversion}-pyproject_hooks >= 1.0.0
Requires:       python%{python3_pkgversion}-requests-toolbelt >= 1.0.0
Requires:       python%{python3_pkgversion}-requests >= 2.26
Requires:       python%{python3_pkgversion}-requests < 3.0
Requires:       python%{python3_pkgversion}-shellingham >= 1.5.0
Requires:       python%{python3_pkgversion}-tomlkit >= 0.11.4
Requires:       python%{python3_pkgversion}-trove-classifiers >= 2022.5.19
Requires:       python%{python3_pkgversion}-virtualenv >= 20.26.6
Requires:       python%{python3_pkgversion}-pbs-installer >= 2025.1.6 
Requires:       python%{python3_pkgversion}-pbs-installer < 2026.0.0
Requires:       python%{python3_pkgversion}-findpython >= 0.6.2
Requires:       python%{python3_pkgversion}-findpython < 0.7.0
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Sun Mar 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.1-1
- Update to 2.1.1

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.4-1
- Update to 1.8.4

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.5.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.5.1-3
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 1.5.1-2
- Update python-shellingham requirement

* Mon Aug 07 2023 Odilon Sousa - 1.5.1-1
- Initial package.