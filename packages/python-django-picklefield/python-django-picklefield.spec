%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name django-picklefield

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.0.1
Release:        5%{?dist}
Summary:        Pickled object field for Django

License:        MIT
URL:            http://github.com/gintas/django-picklefield
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

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
%license LICENSE
%doc README.rst
%{python3_sitelib}/picklefield
%{python3_sitelib}/django_picklefield-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.0.1-5
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.0.1-4
- Build against python 3.11

* Fri May 13 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.1-3
- Obsolete Python 3.8 package

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.1-2
- Build against python 3.9

* Mon Sep 13 2021 Evgeni Golov - 3.0.1-1
- Initial package.
