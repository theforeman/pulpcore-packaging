%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name urlman

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.0.1
Release:        3%{?dist}
Summary:        Django URL pattern helpers

License:        Apache-2.0
URL:            https://github.com/andrewgodwin/urlman
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


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
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.0.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.0.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 2.0.1-1
- Update to 2.0.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.4.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.4.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 1.4.0-1
- Update to 1.4.0

* Thu Nov 05 2020 Evgeni Golov - 1.3.0-2
- Fix License tag in spec file

* Tue Aug 25 2020 Evgeni Golov - 1.3.0-1
- Initial package.
