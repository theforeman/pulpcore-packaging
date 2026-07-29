%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pycparser

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.0
Release:        2%{?dist}
Summary:        C parser in Python

License:        BSD
URL:            https://github.com/eliben/pycparser
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 3.0-2
- Bump release for EL10 rebuild

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.0-1
- Update to 3.0
- Switch to pyproject build; patch pyproject.toml for RHEL9 pip compatibility

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.23-1
- Update to 2.23

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 2.22-2
- Rebuild against python3.12

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.22-1
- Update to 2.22

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.21-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.21-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.21-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.21-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.21-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.21-1
- Release python-pycparser 2.21

* Mon Sep 06 2021 Evgeni Golov - 2.20-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 2.20-1
- Update to 2.20

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.19-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.19-1
- Initial package.
