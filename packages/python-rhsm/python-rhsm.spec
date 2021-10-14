%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name rhsm

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.19.2
Release:        1%{?dist}
Summary:        A Python library to communicate with a Red Hat Unified Entitlement Platform

License:        GPLv2
URL:            http://fedorahosted.org/candlepin
Source0:        %{pypi_source}

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

BuildRequires:  openssl-devel

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-iniparse

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
PYTHON_RHSM_VERSION=%{version} PYTHON_RHSM_RELEASE=%{release} %py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Oct 14 2021 Evgeni Golov - 1.19.2-1
- Initial package.
