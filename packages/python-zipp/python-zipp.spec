%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name zipp

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.4.0
Release:        3%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.4.1


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
%autosetup -n %{pypi_name}-%{version}
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
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 3.4.0-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.4.0-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 3.4.0-1
- Update to 3.4.0

* Thu Jun 04 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 2.1.0-1
- Initial package.
