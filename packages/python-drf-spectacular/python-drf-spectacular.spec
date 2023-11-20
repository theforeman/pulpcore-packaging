%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name drf-spectacular

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.26.5
Release:        2%{?dist}
Summary:        Sane and flexible OpenAPI 3 schema generation for Django REST framework

License:        BSD
URL:            https://github.com/tfranzel/drf-spectacular
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.10.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-inflection >= 0.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jsonschema >= 2.6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uritemplate >= 2.0.0
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
%license LICENSE docs/license.rst
%doc README.rst docs/readme.rst
%{python3_sitelib}/drf_spectacular
%{python3_sitelib}/drf_spectacular-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 0.26.5-2
- Obsolete python39 version

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 0.26.5-1
- Release python-drf-spectacular 0.26.5

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.26.2-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa 0.26.2-1
- Update to 0.26.2

* Fri Feb 03 2023 Odilon Sousa 0.25.0-1
- Update to 0.25.0

* Tue Sep 20 2022 Odilon Sousa 0.23.1-1
- Update to 0.23.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.21.2-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 0.21.2-1
- Release python-drf-spectacular 0.21.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.21.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 0.21.0-1
- Release python-drf-spectacular 0.21.0

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 0.20.1-1
- Release python-drf-spectacular 0.20.1

* Tue Oct 19 2021 Evgeni Golov - 0.17.3-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 0.17.3-2
- Build against Python 3.8

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 0.17.3-1
- Release python-drf-spectacular 0.17.3

* Fri Jul 02 2021 Evgeni Golov - 0.17.2-1
- Release python-drf-spectacular 0.17.2

* Fri Jun 11 2021 Evgeni Golov 0.16.0-1
- Update to 0.16.0

* Fri Mar 19 2021 Evgeni Golov 0.13.2-1
- Update to 0.13.2

* Mon Jan 11 2021 Evgeni Golov 0.11.0-1
- Update to 0.11.0

* Mon Nov 02 2020 Evgeni Golov 0.9.14-1
- Update to 0.9.14

* Mon Sep 28 2020 Evgeni Golov 0.9.13-1
- Update to 0.9.13

* Tue Aug 25 2020 Evgeni Golov - 0.9.12-1
- Initial package.
