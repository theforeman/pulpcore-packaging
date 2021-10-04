%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Markdown
%global srcname markdown

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.3.4
Release:        3%{?dist}
Summary:        Python implementation of Markdown

License:        BSD License
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{srcname} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.md
%{_bindir}/markdown_py
%{python3_sitelib}/markdown
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 29 2021 Evgeni Golov - 3.3.4-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 3.3.4-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.3.4-1
- Update to 3.3.4

* Thu Oct 29 2020 Evgeni Golov 3.3.3-1
- Update to 3.3.3

* Tue Jun 23 2020 Evgeni Golov - 3.2.2-1
- Initial package.
