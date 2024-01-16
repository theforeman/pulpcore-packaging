%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python-dotenv
%global srcname dotenv

Name:           python-%{srcname}
Version:        0.14.0
Release:        11%{?dist}
Summary:        Add .env support to your django/flask apps in development and deployments

License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-click >= 5.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{srcname} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{srcname} < %{version}-%{release}
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


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
%doc README.md
%{_bindir}/dotenv
%{python3_sitelib}/dotenv
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.14.0-11
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.14.0-10
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.14.0-9
- Build against python 3.11

* Thu May 12 2022 Yanis Guenane <yguenane@redhat.com> - 0.14.0-8
- Fix obsolete named package

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.14.0-7
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.14.0-6
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 0.14.0-5
- Obsolete the old Python 3.6 package for smooth upgrade

* Fri Sep 10 2021 Evgeni Golov - 0.14.0-4
- Don't require typing, our Python is new enough

* Wed Sep 08 2021 Evgeni Golov - 0.14.0-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.14.0-2
- Fix License tag in spec file

* Mon Jul 20 2020 Evgeni Golov 0.14.0-1
- Update to 0.14.0

* Tue Apr 28 2020 Evgeni Golov 0.13.0-1
- Update to 0.13.0

* Wed Mar 18 2020 Samir Jha 0.12.0-1
- Update to 0.12.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.10.3-1
- Initial package.
