%global debug_package %{nil}
%{?python_disable_dependency_generator}
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name meson-python
%global pkg_name meson_python

Name:           python-%{pypi_name}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Meson Python build backend (PEP 517)

License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source0:        https://files.pythonhosted.org/packages/source/m/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  meson >= 0.63.3
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-packaging >= 19.0
BuildRequires:  python%{python3_pkgversion}-pyproject-metadata >= 0.7.1
BuildRequires:  pyproject-rpm-macros

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:  meson >= 0.63.3
Requires:  python%{python3_pkgversion}-packaging >= 19.0
Requires:  python%{python3_pkgversion}-pyproject-metadata >= 0.7.1


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pkg_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/mesonpy
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/


%changelog
* Tue Jan 14 2025 Odilon Sousa - 0.16.0-1
- Initial package.
