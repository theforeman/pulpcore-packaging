%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-resumable-media

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.7.2
Release:        1%{?dist}
Summary:        Utilities for Google Media Downloads and Resumable Uploads

License:        Apache 2.0
URL:            https://github.com/googleapis/google-resumable-media-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_resumable_media-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 4~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.6.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth < 2~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 1.22
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-crc32c < 2~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-crc32c >= 1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.18
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 4~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.6.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth < 2~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 1.22
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-crc32c < 2~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-crc32c >= 1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.18


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n google_resumable_media-%{version}
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
%{python3_sitelib}/google_resumable_media-%{version}-py%{python3_version}.egg-info


%changelog
*  - 2.7.2-1
- Initial package.
