%global debug_package %{nil}

%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name rfc3161-client
%global src_name rfc3161_client

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        A client library for RFC 3161 Time-Stamp Protocol

License:        Apache-2.0
URL:            https://github.com/trailofbits/rfc3161-client
Source0:        https://files.pythonhosted.org/packages/source/r/%{src_name}/%{src_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{src_name}-%{version}-vendor.tar.xz
Patch0:         0001-Replace-git-dep-cryptography-x509-with-vendored-vers.patch
Patch1:         0002-Add-cargo-vendor-config.patch
Patch2:         0003-Use-system-openssl-instead-of-vendored.patch

# To create the vendor tarball:
# tar xf %%{src_name}-%%{version}.tar.gz
# pushd %%{src_name}-%%{version}
# cargo vendor --versioned-dirs
# tar Jcf ../%%{src_name}-%%{version}-vendor.tar.xz vendor/
# popd

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-maturin >= 1.7
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cargo
BuildRequires:  openssl-devel
BuildRequires:  rust

Requires:       python%{python3_pkgversion}-cryptography >= 43

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version} -a 1 -p1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitearch}/%{src_name}
%{python3_sitearch}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Sep  3 19:43:45 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.8-1
- Update to 1.0.8
- Regenerate vendor tarball for 1.0.8

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 1.0.6-2
- Bump release for EL10 rebuild

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 1.0.6-1
- Initial package.
