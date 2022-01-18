%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name enrich

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.2.7
Release:        1%{?dist}
Summary:        enrich

License:        MIT
URL:            https://github.com/pycontribs/enrich
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mock >= 3.0.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 5.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov >= 2.7.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mock >= 3.3.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-plus
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist >= 1.29.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rich >= 9.5.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.5.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mock >= 3.0.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 5.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov >= 2.7.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-mock >= 3.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-plus
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist >= 1.29.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-rich >= 9.5.1


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
* Tue Jan 18 2022 Odilon Sousa 1.2.7-1
- Update to 1.2.7

* Wed Oct 20 2021 Evgeni Golov - 1.2.6-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 1.2.6-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov - 1.2.6-1
- Initial package.
