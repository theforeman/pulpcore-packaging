%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name uritemplate

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.2.0
Release:        2%{?dist}
Summary:        Implementation of RFC 6570 URI Templates

License:        BSD 3-Clause License or Apache License, Version 2.0
URL:            https://uritemplate.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

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
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst tests/fixtures/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 4.2.0-2
- Bump release for EL10 rebuild

* Wed Jun 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.2.0-1
- Update to 4.2.0

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 4.1.1-7
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.1.1-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.1.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.1.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.1.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.1.1-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 4.1.1-1
- Update to 4.1.1

* Mon Sep 06 2021 Evgeni Golov - 3.0.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.1-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 3.0.1-1
- Update to 3.0.1

* Mon Nov 18 2019 Evgeni Golov - 3.0.0-1
- Initial package.
