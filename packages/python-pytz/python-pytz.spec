%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pytz

Name:           python-%{pypi_name}
Version:        2022.2.1
Release:        6%{?dist}
Summary:        World timezone definitions, modern and historical

License:        MIT
URL:            http://pythonhosted.org/pytz
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2022.2.1-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2022.2.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2022.2.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2022.2.1-3
- Build against python 3.11

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2022.2.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 2022.2.1-1
- Update to 2022.2.1

* Tue Apr 26 2022 Yanis Guenane - 2021.3-2
- Build against Python 3.9

* Wed Nov 03 2021 Odilon Sousa 2021.3-1
- Update to 2021.3

* Mon Sep 06 2021 Evgeni Golov - 2021.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2021.1-1
- Update to 2021.1

* Mon Nov 02 2020 Evgeni Golov 2020.4-1
- Update to 2020.4

* Tue Apr 28 2020 Evgeni Golov 2020.1-1
- Update to 2020.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2019.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2019.3-1
- Initial package.
