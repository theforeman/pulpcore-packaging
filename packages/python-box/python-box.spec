%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python-box
%global srcname box

Name:           python-%{srcname}
Version:        5.1.0
Release:        7%{?dist}
Summary:        Advanced Python dictionaries with dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-ruamel-yaml
Requires:       python%{python3_pkgversion}-toml


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
%{python3_sitelib}/box
%{python3_sitelib}/python_box-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 5.1.0-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 5.1.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 5.1.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.1.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.1.0-3
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov - 5.1.0-2
- Build against Python 3.8

* Wed Aug 19 2020 Justin Sherrill <jsherril@redhat.com> 5.1.0-1
- update to 5.1.0

* Mon Jul 20 2020 Evgeni Golov 5.0.1-1
- Update to 5.0.1

* Thu Jun 04 2020 Evgeni Golov 4.2.3-1
- Update to 4.2.3

* Wed Mar 18 2020 Samir Jha 4.2.2-1
- Update to 4.2.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.6-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 3.4.6-1
- Update to 3.4.6

* Mon Nov 18 2019 Evgeni Golov - 3.4.5-1
- Initial package.
