%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework

Name:           python-%{pypi_name}
Version:        3.14.0
Release:        4%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            https://www.django-rest-framework.org/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-django-rest-framework = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 3.0
Requires:       python%{python3_pkgversion}-pytz

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif




%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/rest_framework
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.14.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.14.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.14.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.14.0-1
- Update to 3.14.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.13.1-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 3.13.1-1
- Release python-djangorestframework 3.13.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.12.4-5
- Build against python 3.9

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
