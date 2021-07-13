# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-socks

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Proxy connector for aiohttp

License:        Apache 2
URL:            https://github.com/romis2012/aiohttp-socks
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/aiohttp_socks-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-aiohttp >= 2.3.2
Requires:       python%{python3_pkgversion}-attrs >= 19.2.0
Requires:       python%{python3_pkgversion}-socks >= 1.2.2

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n aiohttp_socks-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/aiohttp_socks
%{python3_sitelib}/aiohttp_socks-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov - 0.6.0-1
- Initial package.
