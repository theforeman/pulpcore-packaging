%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name prometheus-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.8.0
Release:        3%{?dist}
Summary:        Python client for the Prometheus monitoring system

License:        Apache Software License 2.0
URL:            https://github.com/prometheus/client_python
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/prometheus_client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n prometheus_client-%{version}
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
%doc README.md
%{python3_sitelib}/prometheus_client
%{python3_sitelib}/prometheus_client-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.8.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.8.0-2
- Build against Python 3.8

* Fri Jul 17 2020 Evgeni Golov - 0.8.0-1
- Initial package.
