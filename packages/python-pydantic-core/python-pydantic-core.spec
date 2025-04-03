%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.8
%global pypi_name pydantic-core
%global srcname pydantic_core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.33.1
Release:        1%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/pydantic/pydantic/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{srcname}-%{version}-vendor.tar.xz
## vendor rust content generated
## tar xf pydantic_core-2.33.1.tar.gz ; pushd pydantic_core-2.33.1 ;  
## cargo vendor-filterer --all-features --platform=x86_64-unknown-linux-gnu && 
## tar Jcvf ../pydantic_core-2.33.1-vendor.tar.xz vendor/ ; popd



BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-maturin
BuildRequires:  python%{python3_pkgversion}-typing-extensions >= 4.6.0
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

Requires:  python%{python3_pkgversion}-typing-extensions >= 4.6.0


%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.33.1-1
- Initial Release

