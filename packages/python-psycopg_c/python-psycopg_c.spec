%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg_c

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.2.3
Release:        2%{?dist}
Summary:        PostgreSQL database adapter for Python - C extension

License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.37

BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  gcc
BuildRequires:  postgresql-devel

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 3.2.3-2
- Rebuild against python3.12

* Wed Oct 09 2024 Evgeni Golov - 3.2.3-1
- Initial package.
