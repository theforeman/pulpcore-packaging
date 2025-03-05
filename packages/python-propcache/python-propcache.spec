%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name propcache

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Fast property caching.

License:        Apache-2.0
URL:            https://github.com/aio-libs/propcache
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-expandvars
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
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
* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.0-1
- Update to 0.3.0

* Mon Dec 16 2024 Odilon Sousa - 0.2.1-1
- Initial package.
