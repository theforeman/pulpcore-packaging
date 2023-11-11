%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name productmd

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.33
Release:        4%{?dist}
Summary:        Product, compose and installation media metadata library

License:        LGPLv2.1
URL:            https://github.com/release-engineering/productmd
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six


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
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.33-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.33-3
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov - 1.33-2
- Build against Python 3.8

* Tue Jun 29 2021 Evgeni Golov - 1.33-1
- Release python-productmd 1.33

* Thu Feb 25 2021 Justin Sherrill <jsherril@redhat.com> 1.31-1
- update to 1.31

* Mon Sep 28 2020 Evgeni Golov 1.28-1
- Update to 1.28

* Tue Aug 25 2020 Evgeni Golov 1.27-1
- Update to 1.27

* Thu Apr 30 2020 Evgeni Golov - 1.26-1
- Initial package.
