%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{?python_disable_dependency_generator}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name jsonschema

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.10.3
Release:        2%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            https://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
#jsonschema switching to strictly pyobject.toml, this is the setup.cfg from 4.5.1
#it's to keep builds working unitl our infrastructure can handle pyboject.toml based building
Source1:        001-SETUP-CFG
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs >= 17.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyrsistent >= 0.14.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.11.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup(use_scm_version=True)' > setup.py
cp %{_topdir}/SOURCES/001-SETUP-CFG setup.cfg
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license json/LICENSE
%doc json/README.md README.rst
%exclude %{_bindir}/jsonschema
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.10.3-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 4.10.3-1
- Release python-jsonschema 4.10.3

* Wed Sep 28 2022 Odilon Sousa <osousa@redhat.com> - 4.9.1-1
- Release python-jsonschema 4.9.1

* Thu Aug 11 2022 Odilon Sousa <osousa@redhat.com> - 4.6.0-4
- Adding dependencie requirement on python-jsonschema for importlib-resources

* Tue Jul 26 2022 Odilon Sousa <osousa@redhat.com> - 4.6.0-1
- Release python-jsonschema 4.6.0 and add a setup.cfg to build on top of EL7

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-8
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 3.2.0-7
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 3.2.0-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.2.0-5
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.2.0-4
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.0-3
- Bump release to build for el8

* Sun Feb 02 2020 Evgeni Golov - 3.2.0-2
- correct jsonschema requires

* Tue Jan 28 2020 Evgeni Golov - 3.2.0-1
- Initial package.
