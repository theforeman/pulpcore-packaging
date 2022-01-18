%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name filelock

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.4.2
Release:        1%{?dist}
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-covdefaults >= 1.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage >= 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-furo >= 2021.8.17b43
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-timeout >= 1.4.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-covdefaults >= 1.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage >= 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-furo >= 2021.8.17b43
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-timeout >= 1.4.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx >= 4.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-autodoc-typehints >= 1.12


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
%license LICENSE docs/license.rst
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 3.4.2-1
- Update to 3.4.2

* Mon Sep 06 2021 Evgeni Golov - 3.0.12-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 3.0.12-1
- Initial package.
