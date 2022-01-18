%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name importlib-resources

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.4.0
Release:        1%{?dist}
Summary:        Read resources from Python packages

License:        None
URL:            https://github.com/python/importlib_resources
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_resources-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jaraco-packaging >= 8.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-black >= 0.3.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-checkdocs >= 2.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-enabler >= 1.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-flake8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rst-linker >= 1.9
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zipp >= 3.1.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jaraco-packaging >= 8.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-black >= 0.3.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-checkdocs >= 2.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-enabler >= 1.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-flake8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-rst-linker >= 1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zipp >= 3.1.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n importlib_resources-%{version}
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
%doc README.rst
%{python3_sitelib}/importlib_resources
%{python3_sitelib}/importlib_resources-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 5.4.0-1
- Update to 5.4.0

* Wed Sep 08 2021 Evgeni Golov - 5.0.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 5.0.0-1
- Initial package.
