%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe
%global srcname markupsafe

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.0.3
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}



%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.3-1
- Update to 3.0.3
- Fix PEP 639 license field incompatibility with RHEL 9 setuptools

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 3.0.2-2
- Rebuild against python3.12

* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.2-1
- Update to 3.0.2

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.1-1
- Update to 3.0.1

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.5-1
- Update to 2.1.5

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2.1.2-1
- Update to 2.1.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.1-3
- Build against python 3.9

* Thu Jan 13 2022 Evgeni Golov - 2.0.1-2
- build markupsafe for Python 3.6 too

* Wed Nov 03 2021 Odilon Sousa 2.0.1-1
- Update to 2.0.1

* Mon Sep 06 2021 Evgeni Golov - 1.1.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.1-1
- Initial package.
