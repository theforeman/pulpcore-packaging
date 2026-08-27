%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name python-dateutil
%global srcname dateutil

Name:           python%{python3_pkgversion}-%{srcname}
Version:        2.9.0.post0
Release:        1%{?dist}
Summary:        Extensions to the standard Python datetime module

License:        Dual License
URL:            https://dateutil.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-six >= 1.5
Requires:       tzdata

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
%{python3_sitelib}/python_dateutil-%{version}.dist-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Thu Aug 27 11:20:29 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.9.0.post0-1
- Update to 2.9.0.post0

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 2.8.2-9
- Bump release for EL10 rebuild

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 2.8.2-8
- Rebuild against python3.12

* Tue Apr 30 2024 Odilon Sousa <osousa@redhat.com> - 2.8.2-7
- Rebuild with new package metadata

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.8.2-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.8.2-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.8.2-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.8.2-3
- Build against python 3.11

* Tue Apr 26 2022 Yanis Guenane - 2.8.2-2
- Build against Python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.8.2-1
- Release python-dateutil 2.8.2

* Wed Sep 08 2021 Evgeni Golov - 2.8.1-4
- Build against Python 3.8

* Mon Aug 24 2020 Evgeni Golov - 2.8.1-3
- Fix Obsoletes

* Thu Aug 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.8.1-2
- Obsolete python36-dateutil

* Fri Jul 17 2020 Evgeni Golov - 2.8.1-1
- Initial package.
