%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python-dateutil
%global srcname dateutil

Name:           python-%{srcname}
Version:        2.8.2
Release:        6%{?dist}
Summary:        Extensions to the standard Python datetime module

License:        Dual License
URL:            https://dateutil.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-six >= 1.5
BuildRequires:  python%{python3_pkgversion}-typing-extensions


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-six >= 1.5
Obsoletes:      python36-dateutil


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/dateutil
%{python3_sitelib}/python_dateutil-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.8.2-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.8.2-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.8.2-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.8.2-3
- Build against python 3.11

* Tue Apr 26 2022 Yanis Guenane - 2.8.2-2
- Build against Python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.8.2-1
- Release python-dateutil 2.8.2

* Wed Sep 08 2021 Evgeni Golov - 2.8.1-4
- Build against Python 3.8

* Mon Aug 24 2020 Evgeni Golov - 2.8.1-3
- Fix Obsoletes

* Thu Aug 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.8.1-2
- Obsolete python36-dateutil

* Fri Jul 17 2020 Evgeni Golov - 2.8.1-1
- Initial package.
