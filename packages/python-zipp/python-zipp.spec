%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name zipp

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.23.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 3.4.1
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = \"\(.*\)\"/license = {text = \"\1\"}/' pyproject.toml
sed -i '/"coherent.licensed"/d' pyproject.toml


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
* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.23.0-1
- Update to 3.23.0
- Fix PEP 639 license field for RHEL 9 pip compatibility

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 3.21.0-2
- Rebuild against python3.12

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.21.0-1
- Update to 3.21.0

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.20.2-1
- Update to 3.20.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.4.0-8
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.4.0-7
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.4.0-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.4.0-5
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.4.0-4
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.4.0-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.4.0-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 3.4.0-1
- Update to 3.4.0

* Thu Jun 04 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 2.1.0-1
- Initial package.
