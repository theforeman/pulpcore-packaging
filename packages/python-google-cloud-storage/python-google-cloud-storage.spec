%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-cloud-storage

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.18.2
Release:        1%{?dist}
Summary:        Google Cloud Storage API client library

License:        Apache 2.0
URL:            https://github.com/googleapis/python-storage
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_cloud_storage-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-api-core < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-api-core >= 2.15
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 2.26.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-cloud-core < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-cloud-core >= 2.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-crc32c < 2~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-crc32c >= 1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-resumable-media >= 2.7.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_api >= 1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-protobuf < 6~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.18
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-api-core < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-api-core >= 2.15
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 2.26.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-cloud-core < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-cloud-core >= 2.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-crc32c < 2~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-crc32c >= 1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-resumable-media >= 2.7.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_api >= 1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf < 6~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.18


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n google_cloud_storage-%{version}
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
%doc README.rst tests/conformance/README.md tests/perf/README.md
%{python3_sitelib}/google
%{python3_sitelib}/google_cloud_storage-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu>  - 2.18.2-1
- Initial package.
