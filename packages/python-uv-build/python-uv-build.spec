%global debug_package %{nil}

%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name uv-build
%global srcname uv_build

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.9.21
Release:        1%{?dist}
Summary:        The uv build backend

License:        %{shrink:
                0BSD AND
                (0BSD OR Apache-2.0 OR MIT) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                Apache-2.0 AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (Apache-2.0 OR MIT) AND
                ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
                ((MIT OR Apache-2.0) AND Unicode-3.0) AND
                (CC0-1.0 OR MIT-0 OR Apache-2.0) AND
                (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
                (MIT OR Apache-2.0 OR Zlib) AND
                (MIT OR Apache-2.0) AND
                (MIT OR Zlib OR Apache-2.0) AND
                MPL-2.0 AND
                Unicode-3.0 AND
                (Unlicense OR MIT) AND
                Zlib
                }
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz

# Generated from the uv_build source distribution in the CS10 sat-pkg-tools
# container with cargo vendor-filterer --all-features. Its Cargo.lock differs
# from uv's, so it needs a separate vendor archive.
Source1:        https://downloads.theforeman.org/vendor/uv_build-%{version}-vendor.tar.xz

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
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/uv-build
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Fri Oct 16 2026 Odilon Sousa <osousa@redhat.com> - 0.9.21-1
- Update python-uv-build to 0.9.21
- Use its own vendor archive and drop the obsolete Git dependency patch
- Record the vendored Rust dependency licenses without cargo-rpm-macros

* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 0.9.7-2
- Bump release for EL10 rebuild

* Thu Apr 02 2026 Odilon Sousa <osousa@redhat.com> - 0.9.7-1
- Initial package
