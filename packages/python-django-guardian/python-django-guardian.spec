%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-guardian

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        8%{?dist}
Summary:        Implementation of per object permissions for Django

License:        BSD
URL:            http://github.com/django-guardian/django-guardian
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.2

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
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/guardian
%{python3_sitelib}/django_guardian-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.4.0-8
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 2.4.0-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.4.0-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 2.4.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.4.0-4
- Build against python 3.9

* Tue Oct 19 2021 Evgeni Golov - 2.4.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 2.4.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Tue Aug 25 2020 Evgeni Golov - 2.3.0-1
- Initial package.
