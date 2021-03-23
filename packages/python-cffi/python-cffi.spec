# Created by pyp2rpm-3.3.3
%global pypi_name cffi

Name:           python-%{pypi_name}
Version:        1.14.5
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code

License:        MIT
URL:            http://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pycparser
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  libffi-devel
BuildRequires:  gcc

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pycparser
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/_cffi_backend.cpython-3*m-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 1.14.5-1
- Update to 1.14.5

* Mon Sep 28 2020 Evgeni Golov 1.14.3-1
- Update to 1.14.3

* Tue Sep 01 2020 Evgeni Golov 1.14.2-1
- Update to 1.14.2

* Mon Aug 10 2020 Evgeni Golov 1.14.1-1
- Update to 1.14.1

* Wed Mar 18 2020 Samir Jha 1.14.0-1
- Update to 1.14.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.13.2-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.13.2-1
- Initial package.
