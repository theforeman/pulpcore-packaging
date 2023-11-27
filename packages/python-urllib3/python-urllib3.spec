%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.26.18
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
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
%license LICENSE.txt
%doc README.rst dummyserver/certs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Nov 27 2023 Odilon Sousa <osousa@redhat.com> - 1.26.18-1
- Release python-urllib3 1.26.18

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.26.8-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.26.8-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.26.8-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 1.26.8-1
- Release python-urllib3 1.26.8

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 1.26.7-1
- Release python-urllib3 1.26.7

* Mon Sep 06 2021 Evgeni Golov - 1.26.6-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 1.26.6-1
- Update to 1.26.6

* Thu Jul 08 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.26.5-1
- Release python-urllib3 1.26.5

* Fri Mar 19 2021 Evgeni Golov 1.26.4-1
- Update to 1.26.4

* Thu Oct 29 2020 Evgeni Golov 1.25.11-1
- Update to 1.25.11

* Mon Aug 10 2020 Evgeni Golov 1.25.10-1
- Update to 1.25.10

* Tue Apr 28 2020 Evgeni Golov 1.25.9-1
- Update to 1.25.9

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.25.8-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 1.25.8-1
- Update to 1.25.8

* Mon Nov 18 2019 Evgeni Golov - 1.25.7-1
- Initial package.
