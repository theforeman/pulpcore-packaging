%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name aiodns

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.5.0
Release:        1%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-pycares >= 4.0.0

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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.0-1
- Update to 3.5.0

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 3.2.0-2
- Rebuild against python3.12

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.0-1
- Update to 3.2.0

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.1.1-1
- Update to 3.1.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.0.0-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.0.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.0.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.0.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.0.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Nov 05 2020 Evgeni Golov - 2.0.0-3
- Fix License tag in spec file

* Wed Apr 01 2020 Evgeni Golov - 2.0.0-2
- Add python%{python3_pkgversion}-typing to Requires

* Wed Mar 18 2020 Samir Jha - 2.0.0-1
- Initial package.
