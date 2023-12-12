%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.6
%global pypi_name aioredis
%global real_version %{version}

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.0.1
Release:        5%{?dist}
Summary:        asyncio (PEP 3156) Redis support

License:        MIT
URL:            https://github.com/aio-libs/aioredis
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{real_version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-async-timeout
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{real_version}
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
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{real_version}-py%{python3_version}.egg-info


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.0.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.0.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.0.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.1-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 2.0.1-1
- Release python-aioredis 2.0.1

* Wed Sep 08 2021 Evgeni Golov - 2.0.0-2
- Build against Python 3.8

* Wed Aug 18 2021 Odilon Sousa <osousa@redhat.com> - 2.0.0-1
- Release python-aioredis 2.0.0

* Tue Jul 13 2021 Evgeni Golov 2.0.0-0.1.b1
- Update to 2.0.0b1

* Fri Jul 02 2021 Evgeni Golov - 2.0.0-0.1.a1
- Initial package.
