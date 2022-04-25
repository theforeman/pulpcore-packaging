%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name inflection

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.5.1
Release:        3%{?dist}
Summary:        A port of Ruby on Rails inflector to Python

License:        MIT
URL:            https://github.com/jpvanhal/inflection
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.5.1-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.5.1-2
- Build against Python 3.8

* Tue Aug 25 2020 Evgeni Golov 0.5.1-1
- Update to 0.5.1

* Thu Jun 18 2020 Evgeni Golov 0.5.0-1
- Update to 0.5.0

* Tue Apr 14 2020 Evgeni Golov 0.4.0-1
- Update to 0.4.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.3.1-1
- Initial package.
