%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name hatchling 

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.31.0
Release:        1%{?dist}
Summary:        This is the extensible, standards compliant build backend used by Hatch.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/tree/master/backend
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pathspec >= 0.10.1
BuildRequires:  python%{python3_pkgversion}-pluggy >= 1.0.0
BuildRequires:  python%{python3_pkgversion}-packaging >= 24.2
BuildRequires:  python%{python3_pkgversion}-trove-classifiers
BuildRequires:  pyproject-rpm-macros


Requires:       python%{python3_pkgversion}-editables >= 0.3
Requires:       python%{python3_pkgversion}-pathspec >= 0.10.1
Requires:       python%{python3_pkgversion}-pluggy >= 1.0.0
Requires:       python%{python3_pkgversion}-packaging >= 24.2
Requires:       python%{python3_pkgversion}-trove-classifiers
Requires:       pyproject-rpm-macros

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
* Sun Aug 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.31.0-1
- Update to 1.31.0

* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 1.29.0-2
- Bump release for EL10 rebuild

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.29.0-1
- Update to 1.29.0

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.27.0-1
- Update to 1.27.0

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 1.21.1-2
- Rebuild against python3.12

* Tue Mar 11 2025 Odilon Sousa <osousa@redhat.com> - 1.21.1-1
- Release python-hatchling 1.21.1

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.18.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.18.0-3
- Build against python 3.11

* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 1.18.0-2
- Add package requirements

* Mon Jul 17 2023 Odilon Sousa - 1.18.0-1
- Initial package.
