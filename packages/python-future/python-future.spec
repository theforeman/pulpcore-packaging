%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name future

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.18.3
Release:        2%{?dist}
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
URL:            https://python-future.org
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%license docs/_themes/LICENSE LICENSE.txt
%doc README.rst
%exclude %{_bindir}/futurize
%exclude %{_bindir}/pasteurize
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/libfuturize
%{python3_sitelib}/libpasteurize
%{python3_sitelib}/past
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.18.3-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 0.18.3-1
- Update to 0.18.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.18.2-5
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.18.2-4
- Build against Python 3.8

* Mon Jan 25 2021 Evgeni Golov - 0.18.2-3
- Don't ship futurize and pasteurize in bin

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.18.2-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 0.18.2-1
- Initial package.
