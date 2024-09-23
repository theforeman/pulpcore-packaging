%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-crc32c

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.6.0
Release:        1%{?dist}
Summary:        A python wrapper of the C library 'Google CRC32C'

License:        Apache 2.0
URL:            https://github.com/googleapis/python-crc32c
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_crc32c-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-resources >= 1.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-resources >= 1.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n google_crc32c-%{version}
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
%doc README.md
%{python3_sitearch}/google_crc32c
%{python3_sitearch}/google_crc32c-%{version}-py%{python3_version}.egg-info


%changelog
*  - 1.6.0-1
- Initial package.
