%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name et-xmlfile

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        An implementation of lxml.xmlfile for the standard library

License:        MIT
URL:            https://bitbucket.org/openpyxl/et_xmlfile
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/et_xmlfile-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n et_xmlfile-%{version}
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
%doc README.rst
%{python3_sitelib}/et_xmlfile
%{python3_sitelib}/et_xmlfile-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 1.0.1-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov - 1.0.1-1
- Initial package.
