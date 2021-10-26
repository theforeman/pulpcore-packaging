%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name bandersnatch

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.4.0
Release:        4%{?dist}
Summary:        Mirroring tool that implements the client (mirror) side of PEP 381

License:        Academic Free License, version 3
URL:            https://github.com/pypa/bandersnatch/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp-socks
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp-xmlrpc
Requires:       %{?scl_prefix}python%{python3_pkgversion}-filelock
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-resources
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i '/setuptools/ s/>40.0.0//' setup.cfg
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
%doc README.md
%{_bindir}/bandersnatch
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/bandersnatch_filter_plugins
%{python3_sitelib}/bandersnatch_storage_plugins
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Oct 26 2021 Evgeni Golov - 4.4.0-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 4.4.0-3
- Build against Python 3.8

* Wed Aug 11 2021 Evgeni Golov - 4.4.0-2
- Patch out setuptools version requirement

* Tue Jul 13 2021 Evgeni Golov - 4.4.0-1
- Initial package.
