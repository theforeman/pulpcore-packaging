%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg2

Name:           python-%{pypi_name}
Version:        2.9.3
Release:        6%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

License:        LGPL with exceptions
URL:            https://psycopg.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  postgresql-devel


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
%license LICENSE doc/src/license.rst doc/COPYING.LESSER
%doc README.rst doc/README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.9.3-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.9.3-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.9.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.9.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.9.3-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 2.9.3-1
- Release python-psycopg2 2.9.3

* Wed Sep 08 2021 Evgeni Golov 2.9.1-1
- Update to 2.9.1

* Mon Sep 06 2021 Evgeni Golov - 2.8.6-2
- Build against Python 3.8

* Mon Sep 07 2020 Evgeni Golov 2.8.6-1
- Update to 2.8.6

* Tue Apr 14 2020 Evgeni Golov 2.8.5-1
- Update to 2.8.5

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.8.4-1
- Initial package.
