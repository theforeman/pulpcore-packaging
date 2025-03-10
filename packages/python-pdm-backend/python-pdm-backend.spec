%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name pdm-backend
%global src_name pdm_backend

Name:           python-%{pypi_name}
Version:        2.4.3
Release:        1%{?dist}
Summary:        The build backend used by PDM that supports latest packaging standards.

License:        MIT license
URL:            https://github.com/pdm-project/pdm-backend
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
Patch:          unbundle-vendored-deps.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-editables
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-tomli_w
BuildRequires:  python%{python3_pkgversion}-pyproject-metadata
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


# Test-only deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  python%{python3_pkgversion}-editables
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-editables
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-tomli_w
Requires:       python%{python3_pkgversion}-pyproject-metadata


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -p1 -n %{src_name}-%{version}
rm -rv src/pdm/backend/_vendor

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

	
%check
git config --global user.name "John Doe"
git config --global user.email "john@doe.com"
%pytest


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Mon Mar 10 2025 Odilon Sousa - 2.4.3-1
- Initial package.
