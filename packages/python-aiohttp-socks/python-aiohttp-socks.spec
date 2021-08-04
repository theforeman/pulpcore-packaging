# Created by pyp2rpm-3.3.7
%global pypi_name aiohttp-socks
%global pypi_version 0.6.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Proxy connector for aiohttp

License:        Apache 2
URL:            https://github.com/romis2012/aiohttp-socks
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/aiohttp_socks-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
The aiohttp-socks package provides a proxy connector for aiohttp.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python%{python3_pkgversion}-aiohttp >= 2.3.2
Requires:       python%{python3_pkgversion}-attrs >= 19.2
Requires:       python%{python3_pkgversion}-python-socks >= 1.2.2
%description -n python3-%{pypi_name}
The aiohttp-socks package provides a proxy connector for aiohttp.

%prep
%autosetup -n aiohttp_socks-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/aiohttp_socks
%{python3_sitelib}/aiohttp_socks-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 03 2021 Odilon Sousa <osousa@redhat.com> - 0.6.0-1
- Initial package.
