%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name yarl

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.8.2
Release:        3%{?dist}
Summary:        Yet another URL library

License:        Apache 2
URL:            https://github.com/aio-libs/yarl/
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-multidict >= 4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.7.4
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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.8.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.8.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.8.2-1
- Update to 1.8.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.7.2-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 1.7.2-1
- Update to 1.7.2

* Wed Sep 08 2021 Evgeni Golov - 1.6.3-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 1.6.3-1
- Update to 1.6.3

* Thu Oct 29 2020 Evgeni Golov 1.6.2-1
- Update to 1.6.2

* Mon Aug 10 2020 Evgeni Golov 1.5.1-1
- Update to 1.5.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Mon Nov 18 2019 Evgeni Golov - 1.3.0-1
- Initial package.
