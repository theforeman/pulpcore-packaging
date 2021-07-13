# Created by pyp2rpm-3.3.3
%global pypi_name python-socks
%global srcname socks

Name:           python-%{srcname}
Version:        1.2.4
Release:        1%{?dist}
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://github.com/romis2012/python-socks
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-async-timeout >= 3.0.1

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/python_socks
%{python3_sitelib}/python_socks-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov - 1.2.4-1
- Initial package.
