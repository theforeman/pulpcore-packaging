%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global debug_package %{nil}

%global pypi_name pysequoia

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.1.35
Release:        1%{?dist}
Summary:        Provides OpenPGP facilities using Sequoia-PGP library

License:        Apache-2.0
URL:            https://github.com/wiktor-k/pysequoia
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.xz

## vendor rust content generated via:
## curl -sL https://files.pythonhosted.org/packages/source/p/pysequoia/pysequoia-0.1.35.tar.gz -o /tmp/pysequoia-0.1.35.tar.gz
## cd /tmp && tar xzf pysequoia-0.1.35.tar.gz && cd pysequoia-0.1.35
## cargo vendor-filterer --all-features --platform=x86_64-unknown-linux-gnu
## tar Jcf ../pysequoia-0.1.35-vendor.tar.xz vendor/

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-maturin >= 1
BuildRequires:  python%{python3_pkgversion}-maturin < 2
BuildRequires:  pyproject-rpm-macros
BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
Provides OpenPGP facilities for Python using the Sequoia PGP library.
Supports signing, verification, encryption, and key management.


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
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
%license LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Sep  2 19:02:18 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.1.35-1
- Update to 0.1.35
- Regenerate vendor tarball for 0.1.35

* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 0.1.34-2
- Bump release for EL10 rebuild

* Wed May 27 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.1.34-1
- Update to 0.1.34
- Regenerate vendor tarball for 0.1.34

* Mon Apr 27 2026 Odilon Sousa <osousa@redhat.com> - 0.1.33-1
- Release python-pysequoia 0.1.33

* Fri Apr 17 2026 Odilon Sousa <osousa@redhat.com> - 0.1.32-1
- Initial package.
- Required by pulp-container >= 2.27.6 for OpenPGP support
