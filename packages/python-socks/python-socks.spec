# Created by pyp2rpm-3.3.7
%global pypi_name python-socks
%global package_name socks
%global srcname socks

Name:           python-%{pypi_name}
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
Python-socks package provides a core proxy client functionality
for Python.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-async-timeout >= 3.0.1
%description -n python3-%{pypi_name}
Python-socks package provides a core proxy client functionality
for Python.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/python_socks
%{python3_sitelib}/python_socks-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 03 2021 Odilon Sousa <osousa@redhat.com> - 1.2.4-1
- Initial package.
