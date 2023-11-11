%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name whitenoise

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        6.0.0
Release:        2%{?dist}
Summary:        Radically simplified static file serving for WSGI applications

License:        MIT
URL:            https://whitenoise.evans.io
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.0.0-2
- Build against python 3.11

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 6.0.0-1
- Release python-whitenoise 6.0.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.3.0-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov 5.3.0-1
- Update to 5.3.0

* Mon Sep 06 2021 Evgeni Golov - 5.2.0-2
- Build against Python 3.8

* Tue Aug 25 2020 Evgeni Golov 5.2.0-1
- Update to 5.2.0

* Thu Jun 04 2020 Evgeni Golov 5.1.0-1
- Update to 5.1.0

* Wed Mar 18 2020 Samir Jha 5.0.1-1
- Update to 5.0.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 4.1.4-1
- Initial package.
