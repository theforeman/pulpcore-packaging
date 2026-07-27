%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name hatch


Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.16.5
Release:        2%{?dist}
Summary:        Modern, extensible Python project management

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling >= 1.27.0
BuildRequires:  python%{python3_pkgversion}-hatch_vcs >= 0.3.0
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli


Requires:  python%{python3_pkgversion}-backports-zstd >= 1.0.0
Requires:  python%{python3_pkgversion}-click >= 8.0.6
Requires:  python%{python3_pkgversion}-discovery >= 1.1
Requires:  python%{python3_pkgversion}-hatchling >= 1.27.0
Requires:  python%{python3_pkgversion}-httpx >= 0.22.0
Requires:  python%{python3_pkgversion}-hyperlink >= 21.0.0
Requires:  python%{python3_pkgversion}-keyring >= 23.5.0
Requires:  python%{python3_pkgversion}-packaging >= 24.2
Requires:  python%{python3_pkgversion}-pexpect >= 4.8
Requires:  python%{python3_pkgversion}-pexpect < 5
Requires:  python%{python3_pkgversion}-platformdirs >= 2.5.0
Requires:  python%{python3_pkgversion}-pyproject_hooks
Requires:  python%{python3_pkgversion}-rich >= 11.2.0
Requires:  python%{python3_pkgversion}-shellingham >= 1.4.0
Requires:  python%{python3_pkgversion}-tomli_w >= 1.0
Requires:  python%{python3_pkgversion}-tomlkit >= 0.11.1
Requires:  python%{python3_pkgversion}-userpath >= 1.7
Requires:  python%{python3_pkgversion}-userpath < 2.0
Requires:  python%{python3_pkgversion}-uv >= 0.5.23
Requires:  python%{python3_pkgversion}-virtualenv >= 21

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 1.16.5-2
- Bump release for EL10 rebuild

* Sun Mar 29 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.16.5-1
- Update to 1.16.5
- Add backports-zstd >= 1.0.0 requirement (replaces zstandard)
- Add python-discovery >= 1.1 requirement
- Add pyproject_hooks requirement
- Update hatchling to >= 1.27.0, packaging to >= 24.2, virtualenv to >= 21

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.15.1-1
- Update to 1.15.1

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.14.2-1
- Update to 1.14.2

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 1.9.7-3
- Rebuild against python3.12

* Fri Mar 14 2025 Odilon Sousa <osousa@redhat.com> - 1.9.7-2
- Fix virtualenv requirement

* Tue Mar 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.9.7-1
- Update to 1.9.7

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.7.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-3
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-2
- Fix tomli_w requirement

* Wed Jul 26 2023 Odilon Sousa - 1.7.0-1
- Initial package.
