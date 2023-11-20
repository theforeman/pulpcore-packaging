%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pyflakes

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.5.0
Release:        1%{?dist}
Summary:        passive checker of Python programs

License:        MIT
URL:            https://github.com/PyCQA/pyflakes
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%exclude %{_bindir}/pyflakes
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-1
- Release python-pyflakes 2.5.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.3.1-6
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.3.1-5
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 2.3.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 2.3.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.3.1-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov 2.3.1-1
- Update to 2.3.1

* Fri Mar 19 2021 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Tue Jun 23 2020 Evgeni Golov - 2.2.0-1
- Initial package.
