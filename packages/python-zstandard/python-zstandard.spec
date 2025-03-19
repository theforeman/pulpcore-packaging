%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name zstandard

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.23.0
Release:        2%{?dist}
Summary:        Python bindings to the Zstandard (zstd) compression library

License:        BSD-3-Clause license
URL:            https://github.com/indygreg/python-zstandard
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.16.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 0.23.0-2
- Rebuild against python3.12

* Mon Mar 10 2025 Odilon Sousa - 0.23.0-1
- Initial package.
