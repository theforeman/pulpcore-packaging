%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name redis

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        6.4.0
Release:        1%{?dist}
Summary:        Python client for Redis database and key-value store

License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Convert PEP 639 SPDX license string to table format for RHEL9 pip compatibility
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 6.4.0-1
- Update to 6.4.0
- Switch to pyproject build (setup.py removed upstream, uses hatchling)
- Fix PEP 639 license format for RHEL9 pip compatibility

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.2.1-1
- Update to 5.2.1

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 5.0.8-2
- Rebuild against python3.12

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.0.8-1
- Update to 5.0.8

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.0.2-1
- Update to 5.0.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.3.4-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.3.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.3.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.3.4-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 4.3.4-1
- Update to 4.3.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.5.3-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.5.3-2
- Build against Python 3.8

* Thu Jun 04 2020 Evgeni Golov 3.5.3-1
- Update to 3.5.3

* Wed Mar 18 2020 Samir Jha 3.4.1-1
- Update to 3.4.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.1.0-1
- Initial package.
