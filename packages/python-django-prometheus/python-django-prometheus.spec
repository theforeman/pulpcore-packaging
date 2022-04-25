%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-prometheus

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.1.0
Release:        3%{?dist}
Summary:        Django middlewares to monitor your application with Prometheus

License:        Apache
URL:            http://github.com/korfuri/django-prometheus
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-prometheus-client >= 0.7


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/"pytest-runner"//' setup.py
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
%doc README.md
%{python3_sitelib}/django_prometheus
%{python3_sitelib}/django_prometheus-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.1.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 2.1.0-2
- Build against Python 3.8

* Tue Aug 25 2020 Evgeni Golov 2.1.0-1
- Update to 2.1.0

* Fri Jul 17 2020 Evgeni Golov - 2.0.0-1
- Initial package.
