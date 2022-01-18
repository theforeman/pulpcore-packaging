%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Markdown
%global srcname markdown

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.3.6
Release:        1%{?dist}
Summary:        Python implementation of Markdown

License:        BSD License
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 4.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyyaml
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 4.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyyaml
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
* Tue Jan 18 2022 Odilon Sousa 3.3.6-1
- Update to 3.3.6

* Fri Nov 05 2021 Satoe Imaishi - 3.3.4-4
- Don't obsolete python 3.6 package and exclude files in bin

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
