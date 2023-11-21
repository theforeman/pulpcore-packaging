%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.8
%global pypi_name python-ldap
%global srcname ldap

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.4.2
Release:        3%{?dist}
Summary:        Python modules for implementing LDAP clients

License:        Python style
URL:            https://www.python-ldap.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyasn1 >= 0.3.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyasn1-modules >= 0.1.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyasn1 >= 0.3.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyasn1-modules >= 0.1.5
Requires:       openldap
Obsoletes: python3-pyldap < 3
Provides:  python3-pyldap = %{version}-%{release}
Provides:  python3-pyldap%{?_isa} = %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{python3_sitearch}/_ldap.cpython-*.so
%{python3_sitearch}/ldapurl.py
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/ldif.py
%{python3_sitearch}/ldap
%{python3_sitearch}/slapdtest
%{python3_sitearch}/python_ldap-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.4.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.4.2-2
- Build against python 3.11

* Wed Aug 24 2022 Odilon Sousa <osousa@redhat.com> - 3.4.2-1
- Initial package.
