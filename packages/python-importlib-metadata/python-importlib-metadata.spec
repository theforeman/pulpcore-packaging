%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name importlib-metadata

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.10.1
Release:        2%{?dist}
Summary:        Read metadata from Python packages

License:        Apache Software License
URL:            http://importlib-metadata.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zipp >= 0.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.6.4

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n importlib_metadata-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup(use_scm_version=True)' > setup.py
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
%{python3_sitelib}/importlib_metadata
%{python3_sitelib}/importlib_metadata-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.10.1-2
- Build against python 3.9

* Wed Feb 23 2022 Odilon Sousa <osousa@redhat.com> - 4.10.1-1
- Release python-importlib-metadata 4.10.1

* Wed Sep 08 2021 Evgeni Golov - 1.7.0-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Thu Jun 18 2020 Evgeni Golov 1.6.1-1
- Update to 1.6.1

* Thu Jun 04 2020 Evgeni Golov 1.6.0-1
- Update to 1.6.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 1.4.0-1
- Initial package.
