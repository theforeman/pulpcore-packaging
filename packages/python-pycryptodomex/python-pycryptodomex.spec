%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pycryptodomex

Name:           python-%{pypi_name}
Version:        3.14.1
Release:        6%{?dist}
Summary:        Cryptographic library for Python

License:        BSD, Public Domain
URL:            https://www.pycryptodome.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%license Doc/LEGAL/copy/LICENSE.libtom Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/src/license.rst LICENSE.rst
%doc README.rst
%{python3_sitearch}/Cryptodome
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.14.1-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.14.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.14.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.14.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.14.1-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa 3.14.1-1
- Update to 3.14.1

* Thu Feb 03 2022 Odilon Sousa 3.14.0-1
- Update to 3.14.0

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.11.0-1
- Release python-pycryptodomex 3.11.0

* Mon Sep 06 2021 Evgeni Golov - 3.10.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.10.1-1
- Update to 3.10.1

* Mon Jul 20 2020 Evgeni Golov 3.9.8-1
- Update to 3.9.8

* Wed Mar 18 2020 Samir Jha 3.9.7-1
- Update to 3.9.7

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.9.6-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 3.9.6-1
- Update to 3.9.6

* Tue Nov 19 2019 Evgeni Golov - 3.9.4-1
- Initial package.
