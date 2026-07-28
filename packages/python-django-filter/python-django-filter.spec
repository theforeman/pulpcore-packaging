%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name django-filter
%global srcname django_filter

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        25.1
Release:        2%{?dist}
Summary:        Django-filter is a reusable Django application for allowing users to filter querysets dynamically

License:        BSD
URL:            https://github.com/carltongibson/django-filter/tree/main
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

Requires:       python%{python3_pkgversion}-django >= 3.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}



%prep
set -ex
%autosetup -n %{srcname}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/django_filters
%{python3_sitelib}/%{srcname}-%{version}.dist-info/


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 25.1-2
- Bump release for EL10 rebuild

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 25.1-1
- Update to 25.1

* Mon Apr 07 2025 Odilon Sousa <osousa@redhat.com> - 24.3-3
- Add obsoletes for python3.11 package

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 24.3-2
- Rebuild against python3.12

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 24.3-1
- Update to 24.3

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
