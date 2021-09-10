%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name python-dotenv
%global srcname dotenv

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.14.0
Release:        4%{?dist}
Summary:        Add .env support to your django/flask apps in development and deployments

License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-click >= 5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click >= 5.0


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
%license LICENSE
%doc README.md
%{_bindir}/dotenv
%{python3_sitelib}/dotenv
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Sep 10 2021 Evgeni Golov - 0.14.0-4
- Don't require typing, our Python is new enough

* Wed Sep 08 2021 Evgeni Golov - 0.14.0-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.14.0-2
- Fix License tag in spec file

* Mon Jul 20 2020 Evgeni Golov 0.14.0-1
- Update to 0.14.0

* Tue Apr 28 2020 Evgeni Golov 0.13.0-1
- Update to 0.13.0

* Wed Mar 18 2020 Samir Jha 0.12.0-1
- Update to 0.12.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.10.3-1
- Initial package.
