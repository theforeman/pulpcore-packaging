%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name python-gnupg
%global src_name python_gnupg
%global srcname gnupg

Name:           python%{python3_pkgversion}-%{srcname}
Version:        0.5.6
Release:        2%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        BSD-3-Clause
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

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

%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/__pycache__/gnupg.*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 0.5.6-2
- Bump release for EL10 rebuild

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.6-1
- Update to 0.5.6
- Fix Source0 URL: use python_gnupg (underscore) as src tarball name

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.4-1
- Update to 0.5.4

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 0.5.3-2
- Rebuild against python3.12

* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.3-1
- Update to 0.5.3

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.2-1
- Update to 0.5.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.5.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.5.0-2
- Build against python 3.11

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 0.5.0-1
- Release python-gnupg 0.5.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.8-2
- Build against python 3.9

* Sat Feb 05 2022 Odilon Sousa <osousa@redhat.com> - 0.4.8-1
- Release python-gnupg 0.4.8

* Fri Sep 03 2021 Evgeni Golov - 0.4.7-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.4.7-1
- Update to 0.4.7

* Tue Apr 28 2020 Evgeni Golov 0.4.6-1
- Update to 0.4.6

* Wed Mar 18 2020 Samir Jha - 0.4.5-1
- Initial package.
