%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global debug_package %{nil}

%global pypi_name rpmrepo-metadata
%global srcname rpmrepo_metadata

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Python bindings for rpmrepo_metadata: create and parse RPM repository metadata

License:        MPL-2.0
URL:            https://github.com/dralley/rpmrepo_metadata
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.gz

# Generated with:
# tar xf %%{srcname}-%%{version}.tar.gz
# pushd %%{srcname}-%%{version}
# cargo vendor --locked --versioned-dirs vendor
# tar czf ../%%{pypi_name}-%%{version}-vendor.tar.gz vendor/

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-maturin >= 1
BuildRequires:  python%{python3_pkgversion}-maturin < 2
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%{?python_provide:%python_provide python%{python3_pkgversion}-rpmrepo-metadata}

%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Fix PEP 639 license fields for RHEL setuptools
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/,/^\]/d' pyproject.toml
%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-rpmrepo-metadata
%license LICENSE.txt
%{python3_sitearch}/rpmrepo_metadata
%{python3_sitearch}/rpmrepo_metadata-%{version}.dist-info/


%changelog
* Mon Sep 21 2026 Odilon Junior <osousa@redhat.com> - 0.7.0-1
- Initial package.
