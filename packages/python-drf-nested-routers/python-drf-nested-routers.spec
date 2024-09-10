%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name drf-nested-routers

Name:           python-%{pypi_name}
Version:        0.93.5
Release:        1%{?dist}
Summary:        Nested resources for the Django Rest Framework

License:        Apache
URL:            https://github.com/alanjds/drf-nested-routers
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 3.2
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.14.0

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
%license LICENSE
%doc README.md README.rst
%{python3_sitelib}/rest_framework_nested
%{python3_sitelib}/rest_framework_nested/runtests
%{python3_sitelib}/drf_nested_routers-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.93.5-1
- Update to 0.93.5

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.93.4-6
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.93.4-5
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.93.4-4
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.93.4-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.93.4-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 0.93.4-1
- Release python-drf-nested-routers 0.93.4

* Tue Oct 19 2021 Evgeni Golov - 0.93.3-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.93.3-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.93.3-1
- Update to 0.93.3

* Mon Nov 02 2020 Evgeni Golov 0.92.1-1
- Update to 0.92.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.91-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.91-1
- Initial package.
