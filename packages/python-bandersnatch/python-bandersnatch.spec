# Created by pyp2rpm-3.3.3
%global pypi_name bandersnatch

Name:           python-%{pypi_name}
Version:        4.4.0
Release:        2%{?dist}
Summary:        Mirroring tool that implements the client (mirror) side of PEP 381

License:        Academic Free License, version 3
URL:            https://github.com/pypa/bandersnatch/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-aiohttp-socks
Requires:       python%{python3_pkgversion}-aiohttp-xmlrpc
Requires:       python%{python3_pkgversion}-filelock
Requires:       python%{python3_pkgversion}-importlib-resources
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i '/setuptools/ s/>40.0.0//' setup.cfg

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/bandersnatch
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/bandersnatch_filter_plugins
%{python3_sitelib}/bandersnatch_storage_plugins
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 11 2021 Evgeni Golov - 4.4.0-2
- Patch out setuptools version requirement

* Tue Jul 13 2021 Evgeni Golov - 4.4.0-1
- Initial package.
