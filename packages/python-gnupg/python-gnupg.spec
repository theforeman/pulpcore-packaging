%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name python-gnupg
%global srcname gnupg

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.4.8
Release:        2%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        BSD-3-Clause
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/gnupg.*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.8-2
- Build against python 3.9

* Sat Feb 05 2022 Odilon Sousa <osousa@redhat.com> - 0.4.8-1
- Release python-gnupg 0.4.8

* Fri Sep 03 2021 Evgeni Golov - 0.4.7-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.4.7-1
- Update to 0.4.7

* Tue Apr 28 2020 Evgeni Golov 0.4.6-1
- Update to 0.4.6

* Wed Mar 18 2020 Samir Jha - 0.4.5-1
- Initial package.
