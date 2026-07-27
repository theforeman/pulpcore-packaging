%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name protobuf

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        6.33.6
Release:        2%{?dist}
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://developers.google.com/protocol-buffers/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

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
%doc README.md
%{python3_sitearch}/google
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 6.33.6-2
- Bump release for EL10 rebuild

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 6.33.6-1
- Update to 6.33.6
- Switch to pyproject_wheel/install (protobuf 6.x builds C extension wheel)
- Fix %files: use sitearch (binary wheel), dist-info; remove nspkg.pth and egg-info (gone in 6.x)

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 5.29.6-1
- Update to 5.29.6

* Sun Jun 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.29.5-1
- Update to 5.29.5

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.29.4-1
- Update to 5.29.4

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 4.25.6-2
- Rebuild against python3.12

* Mon Jan 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.25.6-1
- Update to 4.25.6

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.25.5-1
- Update to 4.25.5

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.25.3-1
- Update to 4.25.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.21.6-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.21.6-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.21.6-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.21.6-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa - 4.21.6-1
- Initial package.
