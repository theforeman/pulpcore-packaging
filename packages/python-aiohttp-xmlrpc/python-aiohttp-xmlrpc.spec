%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-xmlrpc

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        aiohttp XML-RPC server handler and client

License:        MIT
URL:            https://github.com/mosquito/aiohttp-xmlrpc
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp
Requires:       %{?scl_prefix}python%{python3_pkgversion}-lxml


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
%doc README.rst
%{python3_sitelib}/aiohttp_xmlrpc
%{python3_sitelib}/aiohttp_xmlrpc-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 1.5.0-1
- Release python-aiohttp-xmlrpc 1.5.0

* Wed Nov 03 2021 Odilon Sousa <osousa@redhat.com> - 1.3.2-1
- Release python-aiohttp-xmlrpc 1.3.2

* Mon Sep 06 2021 Evgeni Golov - 1.3.1-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov - 1.3.1-1
- Initial package.
