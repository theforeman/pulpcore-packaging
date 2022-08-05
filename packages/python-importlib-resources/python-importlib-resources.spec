%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name importlib-resources

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.0.0
Release:        3%{?dist}
Summary:        Read resources from Python packages

License:        Apache2
URL:            https://github.com/python/importlib_resources
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_resources-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zipp >= 0.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.4.1


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zipp >= 0.4


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n importlib_resources-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Force setuptools_scm usage for older setuptools
sed -i 's/setuptools.setup.*/setuptools.setup(use_scm_version=True)/' setup.py
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
%{python3_sitelib}/importlib_resources-*-py%{python3_version}.egg-info


%changelog
* Fri Aug 05 2022 Odilon Sousa <osousa@redhat.com> - 5.0.0-3
- Force setuptools_scm usage for older setuptools on python-importlib-resources

* Wed Sep 08 2021 Evgeni Golov - 5.0.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 5.0.0-1
- Initial package.
