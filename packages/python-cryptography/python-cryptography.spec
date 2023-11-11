%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        38.0.4
Release:        2%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-cffi = 1.11.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.4.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-rust >= 0.11.4

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%cargo_prep -V 1
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
CRYPTOGRAPHY_DONT_BUILD_RUST=1 %py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE LICENSE.APACHE LICENSE.BSD LICENSE.PSF
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-2
- Build against python 3.11

* Wed Jan 25 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-1
- Release python-cryptography 38.0.4

* Tue Apr 26 2022 Odilon Sousa <osousa@redhat.com> - 3.4.8-1
- Release python-cryptography 3.4.8

* Mon Sep 13 2021 Evgeni Golov - 3.1.1-1
- Release python-cryptography 3.1.1

* Wed Sep 08 2021 Evgeni Golov - 2.9.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 2.9.2-1
- Update to 2.9.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
