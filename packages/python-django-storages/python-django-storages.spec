%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name django-storages

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.14.6
Release:        2%{?dist}
Summary:        Storage backends for Django

License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source0:        https://files.pythonhosted.org/packages/source/d/django_storages/django_storages-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools >= 61.2
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-django >= 3.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
django-storages provides reusable storage backends for Django, including S3
and S3-compatible object stores when boto3 is installed.


%package -n python%{python3_pkgversion}-%{pypi_name}+boto3
Summary:        Metapackage for the django-storages boto3 extra
Requires:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-boto3 >= 1.4.4

%description -n python%{python3_pkgversion}-%{pypi_name}+boto3
This metapackage installs the dependencies required by the django-storages
boto3 extra for S3 and S3-compatible object storage. It contains no code.

%files -n python%{python3_pkgversion}-%{pypi_name}+boto3
%ghost %{python3_sitelib}/django_storages-%{version}.dist-info/


%prep
set -ex
%autosetup -n django_storages-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/storages
%{python3_sitelib}/django_storages-%{version}.dist-info/


%changelog
* Sat Oct 03 2026 Jakub Duchek <jakduch@users.noreply.github.com> - 1.14.6-2
- Restore the package for optional object storage backends
- Add the boto3 extra metapackage for S3-compatible storage
