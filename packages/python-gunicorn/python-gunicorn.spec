%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name gunicorn

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        20.1.0
Release:        6%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        MIT
URL:            https://gunicorn.org
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 3.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif


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
%doc docs/README.rst README.rst
%{_bindir}/gunicorn
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 20.1.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 20.1.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 20.1.0-1
- Update to 20.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.0.4-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 20.0.4-1
- Update to 20.0.4

* Mon Nov 18 2019 Evgeni Golov - 20.0.0-1
- Initial package.
