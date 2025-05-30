%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name uv

Name:           %{pypi_name}
Version:        0.6.5
Release:        2%{?dist}
Summary:        An extremely fast Python package and project manager, written in Rust.


# The license of the uv project is (MIT OR Apache-2.0), except:
#
# Apache-2.0:
#   - crates/uv-python/src/libc.rs contains code derived from
#     crate(glibc_version)
#   - crates/uv-requirements-txt/src/shquote.rs contains code derived from
#     crate(r-shquote); the original code was (Apache-2.0 OR
#     LGPL-2.1-or-later), but the vendored copy cites only the Apache-2.0
#     option.
#
# Apache-2.0 OR BSD-2-Clause:
#   - crates/uv-pep440/ is vendored and forked from crate(pep440_rs)
#   - crates/uv-pep508/ is vendored and forked from crate(pep508_rs)
#   - crates/uv-python/packaging/ is vendored and forked from
#     python3dist(packaging)
#
# (Apache-2.0 OR MIT) AND BSD-3-CLause:
#   - The function wheel_metadata_from_remote_zip in
#     crates/uv-client/src/remote_metadata.rs is vendored and forked from the
#     function lazy_read_wheel_metadata in src/index/lazy_metadata.rs in
#     crate(rattler_installs_packages) and is BSD-3-Clause AND (Apache-2.0 OR
#     MIT): the original routine is BSD-3-CLause, and subsequent modifications
#     are explicitly (Apache-2.0 OR MIT).
#
# MIT
#   - crates/uv-virtualenv/src/activator/ is vendored and forked from
#     python3dist(virtualenv)
#
# Additionally, the following are bundled/forked but happen to be under the
# same (Apache-2.0 OR MIT) terms as uv itself:
#   - crates/uv-extract/src/vendor/cloneable_seekable_reader.rs is vendored and
#     forked from crate(ripunzip)
#
# The following are present in the source but believed not to contribute to the
# licenses of the binary RPMs. Note that ecosystem/ contains only
# pyproject.toml files used for testing, not complete bundled projects.
#
# Apache-2.0:
#   - ecosystem/airflow/
#   - ecosystem/home-assistant-core/
#   - ecosystem/transformers/
#   - ecosystem/warehouse/
# Apache-2.0 OR MIT:
#   - ecosystem/packse/
# BSD-2-Clause-Patent:
#   - ecosystem/github-wikidata-bot/
# BSD-3-Clause:
#   - ecosystem/saleor/
# MIT:
#   - crates/uv-python/fetch-download-metadata.py is derived from
#     https://github.com/mitsuhiko/rye/tree/f9822267a7f00332d15be8551f89a212e7bc9017
#     which was MIT.
#   - ecosystem/black/
#
# Rust crates compiled into the executable contribute additional license terms.
# To obtain the following list of licenses, build the package and note the
# output of %%{cargo_license_summary}. This should automatically include the
# licenses of the following bundled forks:
#   - async_zip, Source100, is MIT.
#   - pubgrub/version-ranges, Source200, is MPL-2.0.
#   - tl, Source400, is MIT.
#
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# ISC AND MIT AND OpenSSL
# LGPL-3.0-or-later OR MPL-2.0
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR LGPL-3.0-or-later
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
                0BSD AND
                (0BSD OR Apache-2.0 OR MIT) AND
                Apache-2.0 AND
                (Apache-2.0 OR BSD-2-Clause) AND
                (Apache-2.0 OR BSD-2-Clause OR MIT) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                (Apache-2.0 OR MIT-0) AND
                (Apache-2.0 WITH LLVM-exception) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                ISC AND
                (LGPL-3.0-or-later OR MIT) AND
                (LGPL-3.0-or-later OR MPL-2.0) AND
                MIT AND
                (MIT OR Unlicense) AND
                MPL-2.0 AND
                OpenSSL AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Zlib
                }
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Generated with tar xf uv-0.6.5.tar.gz ;   
# pushd uv-0.6.5 ;  cargo vendor-filterer --platform=x86_64-unknown-linux-gnu
# && tar Jcvf ../uv-0.6.5-vendor.tar.xz vendor/ ; popd

Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.xz
Patch:         0001-Path-Cargo.toml-for-build-with-vendored-libs.patch


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-maturin >= 1
BuildRequires:  python%{python3_pkgversion}-maturin < 2
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc


%description
%{summary}

%files -n %{pypi_name}
%ghost %{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       uv = %{version}-%{release}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}

%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/uv
# Equivalent to “uv tool run”:
%{_bindir}/uvx
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri May 30 2025 Odilon Sousa <osousa@redhat.com>  - 0.6.5-2
- Add uv metapackage

* Tue Mar 11 2025 Odilon Sousa - 0.6.5-1
- Initial package.
