%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-auth

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.35.0
Release:        1%{?dist}
Summary:        Google Authentication Library

License:        Apache 2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_auth-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 4~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.6.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cachetools < 6~~
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cachetools >= 2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyasn1-modules >= 0.2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyopenssl
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyopenssl >= 20
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyu2f >= 0.1.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.20
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.20
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rsa < 5~~
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rsa >= 3.1.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 4~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.6.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cachetools < 6~~
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cachetools >= 2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyasn1-modules >= 0.2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyopenssl
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyopenssl >= 20
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyu2f >= 0.1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.20
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.20
Requires:       %{?scl_prefix}python%{python3_pkgversion}-rsa < 5~~
Requires:       %{?scl_prefix}python%{python3_pkgversion}-rsa >= 3.1.4


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n google_auth-%{version}
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
%{python3_sitelib}/google
%{python3_sitelib}/google_auth-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.35.0-1
- Initial package.
