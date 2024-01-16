%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name async-lru

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        5%{?dist}
Summary:        Simple lru_cache for asyncio

License:        MIT
URL:            https://github.com/aio-libs/async_lru
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/async_lru.*
%{python3_sitelib}/async_lru.py
%{python3_sitelib}/async_lru-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.3-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 1.0.3-1
- Update to 1.0.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.2-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.2-2
- Build against Python 3.8

* Mon Jan 11 2021 Evgeni Golov - 1.0.2-1
- Initial package.
