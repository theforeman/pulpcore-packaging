%global debug_package %{nil}

%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name uv-build
%global srcname uv_build

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.9.7
Release:        1%{?dist}
Summary:        The uv build backend

License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz

# Shared vendor tarball with python-uv 0.9.7 (same Cargo workspace)
# Generated with: tar xf uv-0.9.7.tar.gz; pushd uv-0.9.7;
# cargo vendor-filterer --platform=x86_64-unknown-linux-gnu &&
# tar Jcvf ../uv-0.9.7-vendor.tar.xz vendor/ ; popd
Source1:        https://downloads.theforeman.org/vendor/uv-%{version}-vendor.tar.xz

Patch0:         0001-Patch-Cargo.toml-for-build-with-vendored-libs.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-maturin >= 1
BuildRequires:  python%{python3_pkgversion}-maturin < 2
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -p1 -n %{srcname}-%{version}
%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/uv-build
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Thu Apr 02 2026 Odilon Sousa <osousa@redhat.com> - 0.9.7-1
- Initial package
