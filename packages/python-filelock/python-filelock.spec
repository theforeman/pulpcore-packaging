%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name filelock

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.29.6
Release:        2%{?dist}
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/benediktschmitt/py-filelock
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

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


%changelog
* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 3.29.6-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.6-1
- Update to 3.29.6

* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.4-1
- Update to 3.29.4

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.1-1
- Update to 3.29.1

* Wed Apr 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.0-1
- Update to 3.29.0

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.25.2-1
- Update to 3.25.2

* Sun Jan 18 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.20.3-1
- Update to 3.20.3

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 3.18.0-2
- Rebuild against python3.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.18.0-1
- Update to 3.18.0

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.17.0-1
- Update to 3.17.0

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.16.1-1
- Update to 3.16.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.8.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.8.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.8.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.8.0-2
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.8.0-1
- Release python-filelock 3.8.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.12-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.0.12-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 3.0.12-1
- Initial package.
