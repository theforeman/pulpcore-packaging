%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-socks

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.7.1
Release:        3%{?dist}
Summary:        Proxy connector for aiohttp

License:        Apache 2
URL:            https://github.com/romis2012/aiohttp-socks
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/aiohttp_socks-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 2.3.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs >= 19.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-socks < 3.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-socks >= 2.0.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n aiohttp_socks-%{version}
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
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/aiohttp_socks
%{python3_sitelib}/aiohttp_socks-%{version}-py%{python3_version}.egg-info


%changelog
* Fri May 06 2022 Odilon Sousa <osousa@redhat.com> - 0.7.1-3
- Rebuilding with python_disable_dependency_generator macro

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.7.1-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa 0.7.1-1
- Update to 0.7.1

* Mon Sep 06 2021 Evgeni Golov - 0.6.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 0.6.0-1
- Initial package.
