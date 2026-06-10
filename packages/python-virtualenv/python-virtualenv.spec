%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name virtualenv


Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        21.4.2
Release:        1%{?dist}
Summary:        A tool for creating isolated virtual python environments.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/virtualenv/tree
Source:         https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:  python%{python3_pkgversion}-discovery >= 1.4
Requires:  python%{python3_pkgversion}-distlib >= 0.3.7
Requires:  python%{python3_pkgversion}-distlib < 1
Requires:  python%{python3_pkgversion}-filelock >= 3.24.2
Requires:  python%{python3_pkgversion}-filelock < 4
Requires:  python%{python3_pkgversion}-platformdirs >= 3.9.1
Requires:  python%{python3_pkgversion}-platformdirs < 5

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 21.4.2-1
- Update to 21.4.2
- Update discovery minimum to >= 1.4 (upstream 21.4.2 requires python-discovery >= 1.4)

* Wed May 27 2026 Foreman Packaging Automation <packaging@theforeman.org> - 21.3.3-1
- Update to 21.3.3
- Update python-discovery lower bound to >= 1.3.1

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 21.3.1-1
- Update to 21.3.1

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 21.2.4-1
- Update to 21.2.4

* Sun Mar 29 2026 Foreman Packaging Automation <packaging@theforeman.org> - 21.2.0-1
- Update to 21.2.0
- Add python-discovery >= 1 requirement (new dep in 21.x)
- Update filelock requirement to >= 3.24.2

* Wed Jan 21 2026 Foreman Packaging Automation <packaging@theforeman.org> - 20.36.1-1
- Update to 20.36.1

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 20.35.4-1
- Update to 20.35.4

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 20.35.3-1
- Update to 20.35.3

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 20.34.0-1
- Update to 20.34.0

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 20.25.3-3
- Add obsoletes for python3.11 package

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 20.25.3-2
- Rebuild against python3.12

* Tue Mar 11 2025 Odilon Sousa <osousa@redhat.com> - 20.25.3-1
- Release python-virtualenv 20.25.3

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 20.24.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.24.2-2
- Build against python 3.11

* Tue Jul 25 2023 Odilon Sousa - 20.24.2-1
- Initial package.