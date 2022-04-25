%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pycryptodomex

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.14.1
Release:        2%{?dist}
Summary:        Cryptographic library for Python

License:        BSD, Public Domain
URL:            https://www.pycryptodome.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
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
%license Doc/LEGAL/copy/LICENSE.libtom Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/src/license.rst LICENSE.rst
%doc README.rst
%{python3_sitearch}/Cryptodome
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
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
