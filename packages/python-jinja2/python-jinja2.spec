%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Jinja2
%global srcname jinja2

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.1.2
Release:        3%{?dist}
Summary:        A very fast and expressive template engine

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        https://files.pythonhosted.org/packages/source/J/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markupsafe >= 2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


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
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/jinja2
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.1.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.1.2-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 3.1.2-1
- Update to 3.1.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.3-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 3.0.3-1
- Release python-jinja2 3.0.3

* Mon Nov 08 2021 Odilon Sousa <osousa@redhat.com> - 3.0.2-1
- Release python-jinja2 3.0.2

* Mon Sep 06 2021 Evgeni Golov - 2.11.3-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.11.3-1
- Update to 2.11.3

* Tue Apr 14 2020 Evgeni Golov 2.11.2-1
- Update to 2.11.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.11.1-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 2.11.1-1
- Update to 2.11.1

* Mon Nov 18 2019 Evgeni Golov - 2.10.3-1
- Initial package.
