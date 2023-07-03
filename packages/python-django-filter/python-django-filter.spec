%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-filter

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        23.2
Release:        1%{?dist}
Summary:        Django-filter is a reusable Django application for allowing users to filter querysets dynamically

License:        BSD
URL:            https://github.com/carltongibson/django-filter/tree/main
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 3.2
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
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
%{python3_sitelib}/django_filters
%{python3_sitelib}/django_filter-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 27 2023 Odilon Sousa 23.2-1
- Update to 23.2

* Mon Sep 26 2022 Odilon Sousa <osousa@redhat.com> - 22.1-2
- Update python-django dependency with right name

* Tue Sep 20 2022 Odilon Sousa 22.1-1
- Update to 22.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 21.1-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 21.1-2
- Build against python 3.9

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 21.1-1
- Release python-django-filter 21.1

* Tue Oct 19 2021 Evgeni Golov - 2.4.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 2.4.0-2
- Build against Python 3.8

* Mon Nov 02 2020 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Tue Aug 25 2020 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
