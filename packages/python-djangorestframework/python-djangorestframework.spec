%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.13.1
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            https://www.django-rest-framework.org/
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
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytz


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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/rest_framework
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 19 2022 Yanis Guenane 3.13.1-1
- Update to 3.13.1

* Tue Oct 19 2021 Evgeni Golov - 3.12.4-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Thu Sep 09 2021 Evgeni Golov - 3.12.4-3
- Correct django-rest-framework Provides to mention Python 3.8

* Wed Sep 08 2021 Evgeni Golov - 3.12.4-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov 3.12.4-1
- Update to 3.12.4

* Mon Jan 11 2021 Evgeni Golov 3.12.2-1
- Update to 3.12.2

* Mon Dec 21 2020 Evgeni Golov - 3.12.1-2
- Add provides for python3-django-rest-framework

* Mon Nov 02 2020 Evgeni Golov 3.12.1-1
- Update to 3.12.1

* Thu Oct 29 2020 Evgeni Golov 3.11.2-1
- Update to 3.11.2

* Mon Sep 28 2020 Evgeni Golov 3.11.1-1
- Update to 3.11.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.10.3-1
- Initial package.
