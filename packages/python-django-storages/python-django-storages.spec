%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-storages

Name:           python-%{pypi_name}
Version:        1.14.4
Release:        1%{?dist}
Summary:        Support for many storage backends in Django

License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
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
Requires:       python%{python3_pkgversion}-azure-storage-blob >= 12.0.0
Requires:       python%{python3_pkgversion}-boto3 >= 1.4.4

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
%doc README.rst
%{python3_sitelib}/storages
%{python3_sitelib}/django_storages-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.14.4-1
- Update to 1.14.4

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.12.3-5
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.12.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.12.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.12.3-2
- Build against python 3.9

* Tue Nov 02 2021 Evgeni Golov - 1.12.3-1
- Release python-django-storages 1.12.3

* Wed Oct 27 2021 Evgeni Golov - 1.11.1-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 1.11.1-1
- Initial package.
