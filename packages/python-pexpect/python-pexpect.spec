%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pexpect

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.9.0
Release:        2%{?dist}
Summary:        Pexpect allows easy control of interactive console applications

License:        ISC license
URL:            https://pexpect.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-ptyprocess

BuildArch:      noarch

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
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 4.9.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.9.0-1
- Update to 4.9.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.8.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.8.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.8.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.8.0-3
- Build against python 3.11

* Thu Sep 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.8.0-2
- Add requires on python-ptyprocess

* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.8.0-1
- Initial package.
