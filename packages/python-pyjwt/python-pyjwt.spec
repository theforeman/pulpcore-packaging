%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name PyJWT
%global srcname pyjwt

Name:           python%{python3_pkgversion}-%{srcname}
Version:        2.12.1
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python

License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Provides:       python%{python3_pkgversion}-jwt = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-jwt < %{version}-%{release}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%package -n python%{python3_pkgversion}-%{srcname}+crypto
Summary: Metapackage for python3-pyjwt: crypto extra
Requires: python%{python3_pkgversion}-cryptography >= 3.4.0

%description -n python%{python3_pkgversion}-%{srcname}+crypto
This is a metapackage bringing in crypto extra requires for python%{python3_pkgversion}-%{srcname}
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{srcname}+crypto
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# Convert PEP 639 SPDX license string to dict format for RHEL 9 setuptools compatibility
sed -i 's/^license = "\(.*\)"$/license = {text = "\1"}/' pyproject.toml
# Lower minimum setuptools version to what RHEL 9 provides
sed -i 's/setuptools>=77.0.3/setuptools>=68/' pyproject.toml

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%exclude %{_bindir}/pyjwt
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.12.1-1
- Update to 2.12.1
- Fix PEP 639 license string and lower setuptools requirement for RHEL 9 buildroot

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.10.1-1
- Update to 2.10.1

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 2.9.0-4
- Fix metapackage metadata

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 2.9.0-3
- Provides metapackage crypto

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 2.9.0-2
- Rebuild against python3.12

* Wed Dec 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.9.0-1
- Update to 2.9.0

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.0-1
- Update to 2.8.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.5.0-5
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.5.0-3
- Build against python 3.11

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.5.0-2
- Adding new dependency for python-pyjwt

* Tue Sep 20 2022 Odilon Sousa 2.5.0-1
- Update to 2.5.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.7.1-8
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 1.7.1-7
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 1.7.1-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 22 2021 Evgeni Golov - 1.7.1-5
- Correct provides for Python 3.8

* Mon Sep 06 2021 Evgeni Golov - 1.7.1-4
- Build against Python 3.8

* Thu Aug 27 2020 Evgeni Golov - 1.7.1-3
- Obsolete python3-jwt

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.7.1-1
- Initial package.
