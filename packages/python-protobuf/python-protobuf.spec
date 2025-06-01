%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name protobuf

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        5.29.5
Release:        1%{?dist}
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://developers.google.com/protocol-buffers/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitearch}/google
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Jun 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.29.5-1
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
