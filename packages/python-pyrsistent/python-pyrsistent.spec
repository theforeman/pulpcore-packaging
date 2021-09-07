%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pyrsistent

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.17.3
Release:        2%{?dist}
Summary:        Persistent/Functional/Immutable data structures

License:        MIT
URL:            http://github.com/tobgu/pyrsistent/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%doc README.rst
%{python3_sitearch}/__pycache__/_pyrsistent_version.*
%{python3_sitearch}/_pyrsistent_version.py
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/pvectorc.cpython-3*-x86_64-linux-gnu.so


%changelog
* Mon Sep 06 2021 Evgeni Golov - 0.17.3-2
- Build against Python 3.8

* Thu Oct 29 2020 Evgeni Golov 0.17.3-1
- Update to 0.17.3

* Thu Sep 10 2020 Evgeni Golov 0.17.2-1
- Update to 0.17.2

* Wed Sep 09 2020 Evgeni Golov 0.17.0-1
- Update to 0.17.0

* Thu Jun 04 2020 Evgeni Golov 0.16.0-1
- Update to 0.16.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.15.7-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 0.15.7-1
- Initial package.
