%global debug_package %{nil}

%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name nh3

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.3.6
Release:        1%{?dist}
Summary:        Python binding to Ammonia HTML sanitizer Rust crate

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/messense/nh3
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.xz

#To create the vendor tarball:#
# tar xf %%{name}-%%{version}.tar.gz ; pushd %%{name}-%%{version} ; \ 
# cargo vendor --versioned-dirs --platform=x86_64-unknown-linux-gnu --version && \
# tar Jcvf ../%%{name}-%%{version}-vendor.tar.xz vendor/ ; popd

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-maturin
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
Python bindings to the ammonia HTML sanitization library.

nh3 is about 20 times faster than the deprecated bleach package and offers
Python bindings to the ammonia HTML sanitization library with many options
to customize the sanitization.

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.6-1
- Update to 0.3.6

* Sun Apr 26 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.5-1
- Update to 0.3.5

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.4-1
- Update to 0.3.4
- Fix PEP 639 license field in pyproject.toml for RHEL 9 setuptools

* Tue Sep 23 2025 Odilon Sousa <osousa@redhat.com> - 0.3.0-1
- Initial package. 
