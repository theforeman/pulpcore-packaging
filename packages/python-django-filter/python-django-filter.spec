%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-filter
%global srcname django_filters

Name:           python-%{pypi_name}
Version:        23.5
Release:        1%{?dist}
Summary:        Django-filter is a reusable Django application for allowing users to filter querysets dynamically

License:        BSD
URL:            https://github.com/carltongibson/django-filter/tree/main
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core



%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 3.2

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/django_filter-%{version}.dist-info/


%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 23.5-1
- Update to 23.5

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 23.2-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 23.2-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 23.2-2
- Build against python 3.11

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
