%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pypi-simple

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.9.0
Release:        3%{?dist}
Summary:        PyPI Simple Repository API client library

License:        MIT
URL:            https://github.com/jwodder/pypi-simple
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:  %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:  %{?scl_prefix}python%{python3_pkgversion}-requests
Requires:  %{?scl_prefix}python%{python3_pkgversion}-beautifulsoup4


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup()' > setup.py
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
%{python3_sitelib}/pypi_simple
%{python3_sitelib}/pypi_simple-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.9.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.9.0-2
- Build against python 3.9

* Tue Feb 22 2022 Evgeni Golov - 0.9.0-1
- Initial package.
