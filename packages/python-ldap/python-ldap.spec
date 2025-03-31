%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name python-ldap
%global srcname ldap

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.4.2
Release:        6%{?dist}
Summary:        Python modules for implementing LDAP clients

License:        Python style
URL:            https://www.python-ldap.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyasn1 >= 0.3.7
BuildRequires:  python%{python3_pkgversion}-pyasn1-modules >= 0.1.5
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel

Requires:       python%{python3_pkgversion}-pyasn1 >= 0.3.7
Requires:       python%{python3_pkgversion}-pyasn1-modules >= 0.1.5
Requires:       openldap
Obsoletes: python3-pyldap < 3
Provides:  python3-pyldap = %{version}-%{release}
Provides:  python3-pyldap%{?_isa} = %{version}-%{release}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}



%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitearch}/_ldap.cpython-*.so
%{python3_sitearch}/ldapurl.py
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/ldif.py
%{python3_sitearch}/ldap
%{python3_sitearch}/slapdtest
%{python3_sitearch}/python_ldap-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 3.4.2-6
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.4.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.4.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.4.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.4.2-2
- Build against python 3.11

* Wed Aug 24 2022 Odilon Sousa <osousa@redhat.com> - 3.4.2-1
- Initial package.
