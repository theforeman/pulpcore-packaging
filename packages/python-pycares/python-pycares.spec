%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pycares

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.1.2
Release:        2%{?dist}
Summary:        Python interface for c-ares

License:        MIT
URL:            http://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.1


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
%license LICENSE deps/c-ares/LICENSE.md
%doc PYPIREADME.rst README.rst deps/c-ares/README.cares deps/c-ares/README.md deps/c-ares/README.msvc deps/c-ares/test/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.1.2-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 4.1.2-1
- Update to 4.1.2

* Wed Sep 08 2021 Evgeni Golov - 4.0.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 4.0.0-1
- Update to 4.0.0

* Thu Nov 05 2020 Evgeni Golov - 3.1.1-2
- Fix License tag in spec file

* Wed Mar 18 2020 Samir Jha - 3.1.1-1
- Initial package.
