%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name django-auth-ldap

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.0.0
Release:        6%{?dist}
Summary:        Django LDAP authentication backend

License:        BSD
URL:            https://github.com/django-auth-ldap/django-auth-ldap
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm

Requires:       python%{python3_pkgversion}-django >= 2.2
Requires:       python%{python3_pkgversion}-ldap >= 3.1

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}



%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# create a minimal setup.py, the rest will be done by setuptools
printf 'from setuptools import setup\nsetup(use_scm_version=True)' > setup.py


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_auth_ldap
%{python3_sitelib}/django_auth_ldap-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Apr 07 2025 Odilon Sousa <osousa@redhat.com> - 4.0.0-6
- Add obsoletes for python3.11 package

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 4.0.0-5
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.0.0-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.0.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.0.0-2
- Build against python 3.11

* Wed Aug 24 2022 Odilon Sousa <osousa@redhat.com> - 4.0.0-1
- Initial package.
