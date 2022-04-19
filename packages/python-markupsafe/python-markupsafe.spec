%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe
%global srcname markupsafe

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 19 2022 Yanis Guenane 2.1.1-1
- Update to 2.1.1

* Thu Jan 13 2022 Evgeni Golov - 2.0.1-2
- build markupsafe for Python 3.6 too

* Wed Nov 03 2021 Odilon Sousa 2.0.1-1
- Update to 2.0.1

* Mon Sep 06 2021 Evgeni Golov - 1.1.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.1-1
- Initial package.
