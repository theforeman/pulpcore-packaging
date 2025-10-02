%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name poetry

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.2.1
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
BuildRequires:  python%{python3_pkgversion}-poetry_core >= 2.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-poetry_core ==  %{version}
Requires:       python%{python3_pkgversion}-build >= 1.2.1
Requires:       python%{python3_pkgversion}-build < 2.0.0
Requires:       python%{python3_pkgversion}-cachecontrol >= 0.14.0
Requires:       python%{python3_pkgversion}-cachecontrol < 0.15.0
Requires:       python%{python3_pkgversion}-cleo >= 2.1.0
Requires:       python%{python3_pkgversion}-cleo < 3.0.0
Requires:       python%{python3_pkgversion}-dulwich >= 0.24.0
Requires:       python%{python3_pkgversion}-dulwich < 0.25.0
Requires:       python%{python3_pkgversion}-fastjsonschema >= 2.18.0
Requires:       python%{python3_pkgversion}-fastjsonschema < 3.0.0
Requires:       python%{python3_pkgversion}-installer >= 0.7.0
Requires:       python%{python3_pkgversion}-installer < 0.8.0
Requires:       python%{python3_pkgversion}-keyring >= 25.1.0
Requires:       python%{python3_pkgversion}-keyring < 26.0.0
Requires:       python%{python3_pkgversion}-packaging >= 24.2
Requires:       python%{python3_pkgversion}-pkginfo >= 1.12
Requires:       python%{python3_pkgversion}-pkginfo < 2.0
Requires:       python%{python3_pkgversion}-platformdirs >= 3.0.0
Requires:       python%{python3_pkgversion}-platformdirs < 5
Requires:       python%{python3_pkgversion}-pyproject_hooks >= 1.0.0
Requires:       python%{python3_pkgversion}-pyproject_hooks < 2.0.0
Requires:       python%{python3_pkgversion}-requests >= 2.26
Requires:       python%{python3_pkgversion}-requests < 3.0
Requires:       python%{python3_pkgversion}-requests-toolbelt >= 1.0.0
Requires:       python%{python3_pkgversion}-requests-toolbelt < 2.0.0
Requires:       python%{python3_pkgversion}-shellingham >= 1.5
Requires:       python%{python3_pkgversion}-shellingham < 2.0
Requires:       python%{python3_pkgversion}-tomlkit >= 0.11.4
Requires:       python%{python3_pkgversion}-tomlkit < 1.0.0
Requires:       python%{python3_pkgversion}-trove-classifiers >= 2022.5.19
Requires:       python%{python3_pkgversion}-virtualenv >= 20.26.6
Requires:       python%{python3_pkgversion}-findpython >= 0.6.2
Requires:       python%{python3_pkgversion}-findpython < 0.8.0
Requires:       python%{python3_pkgversion}-pbs_installer >= 2025.1.6
Requires:       python%{python3_pkgversion}-pbs_installer < 2026.0.0

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.1-1
- Update to 2.2.1

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-6
- Drop python-lockfile

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-5
- Drop jsonschema from requirement

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-4
- Rebuild against python3.12

* Fri Mar 14 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-3
- Fix poetry_core requirement

* Fri Mar 14 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-2
- Fix virtualenv requirement

* Thu Mar 13 2025 Odilon Sousa <osousa@redhat.com> - 1.8.3-1
- Release python-poetry 1.8.3

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.5.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.5.1-3
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 1.5.1-2
- Update python-shellingham requirement

* Mon Aug 07 2023 Odilon Sousa - 1.5.1-1
- Initial package.