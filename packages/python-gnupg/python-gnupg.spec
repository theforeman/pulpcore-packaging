%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python-gnupg
%global srcname gnupg

Name:           python-%{srcname}
Version:        0.5.3
Release:        1%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        BSD-3-Clause
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup()' > setup.py


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/gnupg.*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.3-1
- Update to 0.5.3

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.2-1
- Update to 0.5.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.5.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.5.0-2
- Build against python 3.11

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 0.5.0-1
- Release python-gnupg 0.5.0

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
