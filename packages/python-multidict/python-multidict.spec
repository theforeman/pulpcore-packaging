%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name multidict

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.2.0
Release:        1%{?dist}
Summary:        multidict implementation

License:        Apache 2
URL:            https://github.com/aio-libs/multidict
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Nov 03 2021 Odilon Sousa 5.2.0-1
- Update to 5.2.0

* Mon Sep 06 2021 Evgeni Golov - 5.1.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 5.1.0-1
- Update to 5.1.0

* Thu Oct 29 2020 Evgeni Golov 5.0.0-1
- Update to 5.0.0

* Thu Jun 04 2020 Evgeni Golov 4.7.6-1
- Update to 4.7.6

* Wed Mar 18 2020 Samir Jha 4.7.5-1
- Update to 4.7.5

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.7.4-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 4.7.4-1
- Update to 4.7.4

* Mon Jan 06 2020 Evgeni Golov 4.7.3-1
- Update to 4.7.3

* Fri Dec 13 2019 Evgeni Golov 4.7.1-1
- Update to 4.7.1

* Mon Nov 18 2019 Evgeni Golov - 4.5.2-1
- Initial package.
