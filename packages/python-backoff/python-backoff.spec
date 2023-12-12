%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name backoff

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.2.1
Release:        4%{?dist}
Summary:        Function decoration for backoff and retry

License:        MIT
URL:            https://github.com/litl/backoff
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.2.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.2.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.2.1-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2.2.1-1
- Update to 2.2.1

* Tue Sep 20 2022 Odilon Sousa 2.1.2-1
- Update to 2.1.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.11.1-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov 1.11.1-1
- Update to 1.11.1

* Mon Sep 06 2021 Evgeni Golov - 1.10.0-4
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.10.0-3
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.10.0-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.10.0-1
- Update to 1.10.0

* Mon Nov 18 2019 Evgeni Golov - 1.9.0-1
- Initial package.
