%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name jsonschema

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.2.0
Release:        5%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            https://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs >= 17.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyrsistent >= 0.14.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.11.0


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
%license json/LICENSE
%doc json/README.md README.rst
%{_bindir}/jsonschema
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 3.2.0-5
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.2.0-4
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.0-3
- Bump release to build for el8

* Sun Feb 02 2020 Evgeni Golov - 3.2.0-2
- correct jsonschema requires

* Tue Jan 28 2020 Evgeni Golov - 3.2.0-1
- Initial package.
