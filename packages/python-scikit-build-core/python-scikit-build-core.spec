%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name scikit-build-core
%global srcname scikit_build_core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.11.1
Release:        2%{?dist}
Summary:        Build backend for CMake based projects

License:        MIT License
URL:            https://github.com/scikit-build/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling >= 0.21.1
BuildRequires:  python%{python3_pkgversion}-hatch_vcs

Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-packaging
Requires: python%{python3_pkgversion}-pathspec
Requires: python%{python3_pkgversion}-wheel


%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}



%prep
set -ex
%autosetup -n %{srcname}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/scikit_build_core
%{python3_sitelib}/%{srcname}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 0.11.1-2
- Bump release for EL10 rebuild

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> -  0.11.1-1
- Initial package.
