%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name sqlparse

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.4.4
Release:        3%{?dist}
Summary:        A non-validating SQL parser

License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        001-SETUP-CFG
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup()' > setup.py
cp %{_topdir}/SOURCES/001-SETUP-CFG setup.cfg
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE docs/source/license.rst
%doc README.rst
%exclude %{_bindir}/sqlformat
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.4-2
- Build against python 3.11

* Mon Jun 12 2023 Odilon Sousa <osousa@redhat.com> - 0.4.4-1
- Release python-sqlparse 0.4.4
- Add setup.cfg and setup.py to build package on EL8

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-3
- Build against python 3.9

* Mon Nov 29 2021 Odilon Sousa <osousa@redhat.com> - 0.4.2-2
- Release python-sqlparse 0.4.2

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.4.2-1
- Release python-sqlparse 0.4.2

* Fri Nov 05 2021 Satoe Imaishi - 0.4.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 0.4.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.4.1-2
- Build against Python 3.8

* Thu Oct 29 2020 Evgeni Golov 0.4.1-1
- Update to 0.4.1

* Wed Mar 18 2020 Samir Jha 0.3.1-1
- Update to 0.3.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.3.0-1
- Initial package.
