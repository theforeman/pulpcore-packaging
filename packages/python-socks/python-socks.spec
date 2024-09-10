%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python_socks
%global srcname socks

Name:           python-%{srcname}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://github.com/romis2012/python-socks
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-async-timeout >= 3.0.1


%description -n python%{python3_pkgversion}-%{srcname}
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


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/python_socks
%{python3_sitelib}/python_socks-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 10 2024 Odilon Sousa <osousa@redhat.com> - 2.5.1-1
- Release python-socks 2.5.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.0.3-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.0.3-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.0.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.0.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.3-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.0.3-1
- Release python-socks 2.0.3

* Mon Sep 06 2021 Evgeni Golov - 1.2.4-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 1.2.4-1
- Initial package.
