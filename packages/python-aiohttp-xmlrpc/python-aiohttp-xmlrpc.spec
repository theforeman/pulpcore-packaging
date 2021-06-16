# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-xmlrpc

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        1%{?dist}
Summary:        aiohttp XML-RPC server handler and client

License:        MIT
URL:            https://github.com/mosquito/aiohttp-xmlrpc
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-lxml

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitelib}/aiohttp_xmlrpc
%{python3_sitelib}/aiohttp_xmlrpc-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 11 2021 Evgeni Golov - 1.3.1-1
- Initial package.
