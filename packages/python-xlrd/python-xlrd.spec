%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name xlrd

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        9%{?dist}
Summary:        Library for developers to extract data from Microsoft Excel (tm)

License:        BSD
URL:            http://www.python-excel.org/
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%exclude %{_bindir}/runxlrd.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.0.1-9
- Remove SCL bits

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 2.0.1-8
- Dont obsolete python39-xlrd

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.0.1-7
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.0.1-6
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.1-5
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 2.0.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 2.0.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.0.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.0.1-1
- Update to 2.0.1

* Tue Apr 28 2020 Evgeni Golov - 1.2.0-1
- Initial package.
