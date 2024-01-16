%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pygtrie

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        5%{?dist}
Summary:        A pure Python trie data structure implementation

License:        Apache-2.0
URL:            https://github.com/mina86/pygtrie
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


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.5.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.5.0-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 2.5.0-1
- Update to 2.5.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.4.2-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 2.4.2-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.4.2-1
- Update to 2.4.2

* Tue Apr 14 2020 Evgeni Golov 2.3.3-1
- Update to 2.3.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov - 2.3.2-1
- Initial package.
