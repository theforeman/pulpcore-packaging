%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name url-normalize

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.4.3
Release:        3%{?dist}
Summary:        URL normalization for Python

License:        MIT
URL:            https://github.com/niksite/url-normalize
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%{python3_sitelib}/url_normalize
%{python3_sitelib}/url_normalize-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 1.4.3-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.4.3-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 1.4.3-1
- Update to 1.4.3

* Tue Aug 25 2020 Evgeni Golov - 1.4.2-1
- Initial package.
