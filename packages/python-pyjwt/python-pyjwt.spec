%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name PyJWT
%global srcname pyjwt

Name:           %{?scl_prefix}python-%{srcname}
Version:        1.7.1
Release:        6%{?dist}
Summary:        JSON Web Token implementation in Python

License:        MIT
URL:            http://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       %{?scl_prefix}python%{python3_pkgversion}-jwt = %{version}-%{release}
Obsoletes:      %{?scl_prefix}python%{python3_pkgversion}-jwt < %{version}-%{release}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 1.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{srcname} < %{version}-%{release}
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
%license LICENSE
%doc README.rst
%{_bindir}/pyjwt
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 29 2021 Evgeni Golov - 1.7.1-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 22 2021 Evgeni Golov - 1.7.1-5
- Correct provides for Python 3.8

* Mon Sep 06 2021 Evgeni Golov - 1.7.1-4
- Build against Python 3.8

* Thu Aug 27 2020 Evgeni Golov - 1.7.1-3
- Obsolete python3-jwt

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.7.1-1
- Initial package.
