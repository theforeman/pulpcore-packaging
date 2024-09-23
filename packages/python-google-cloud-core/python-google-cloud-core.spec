%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-cloud-core

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.4.1
Release:        1%{?dist}
Summary:        Google Cloud API client core library

License:        Apache 2.0
URL:            https://github.com/googleapis/python-cloud-core
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2 with python%{python3_pkgversion}-google-api-core < 2.1)
BuildConflicts: %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2.1 with python%{python3_pkgversion}-google-api-core < 2.2)
BuildConflicts: %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2.2 with python%{python3_pkgversion}-google-api-core < 2.3)
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-google-api-core = 2.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-api-core < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-api-core >= 1.31.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth < 3~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 1.25
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-grpcio < 2~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-grpcio >= 1.38
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-grpcio-status < 2~~dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-grpcio-status >= 1.38
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata > 1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Conflicts:      %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2 with python%{python3_pkgversion}-google-api-core < 2.1)
Conflicts:      %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2.1 with python%{python3_pkgversion}-google-api-core < 2.2)
Conflicts:      %{?scl_prefix}(python%{python3_pkgversion}-google-api-core >= 2.2 with python%{python3_pkgversion}-google-api-core < 2.3)
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-google-api-core = 2.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-api-core < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-api-core >= 1.31.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth < 3~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-google-auth >= 1.25
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio < 2~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio >= 1.38
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio-status < 2~~dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio-status >= 1.38
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata > 1.0


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
%{python3_sitelib}/google
%{python3_sitelib}/google_cloud_core-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.4.1-1
- Initial package.
