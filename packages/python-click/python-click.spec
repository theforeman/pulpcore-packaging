%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name click

Name:           python-%{pypi_name}
Version:        8.1.7
Release:        1%{?dist}
Summary:        Composable command line interface toolkit

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/click/
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 8.1.7-1
- Update to 8.1.7

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 8.1.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 8.1.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 8.1.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 8.1.3-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 8.1.3-1
- Update to 8.1.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 8.0.3-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 8.0.3-1
- Update to 8.0.3

* Wed Sep 08 2021 Evgeni Golov 8.0.1-1
- Update to 8.0.1

* Mon Sep 06 2021 Evgeni Golov - 7.1.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 7.1.2-1
- Update to 7.1.2

* Wed Mar 18 2020 Samir Jha 7.1.1-1
- Update to 7.1.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 7.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 7.0-1
- Initial package.
