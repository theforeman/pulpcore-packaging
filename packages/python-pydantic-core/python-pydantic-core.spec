%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.8
%global pypi_name pydantic-core
%global srcname pydantic_core

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.41.5
Release:        1%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/pydantic/pydantic/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{srcname}-%{version}-vendor.tar.gz
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
# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
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
* Thu Apr 02 2026 Odilon Sousa <osousa@redhat.com> - 2.41.5-1
- Release python-pydantic-core 2.41.5

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.33.2-1
- Update to 2.33.2
- Fix PEP 639 license field in pyproject.toml for RHEL 9 setuptools
- Fix Source1: vendor tarball uses .tar.gz format for 2.33.2

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.33.1-1
- Initial Release

