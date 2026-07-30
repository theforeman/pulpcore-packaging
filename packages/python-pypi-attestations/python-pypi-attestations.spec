%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pypi-attestations
%global src_name pypi_attestations

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.0.28
Release:        2%{?dist}
Summary:        A library to convert between Sigstore Bundles and PEP-740 Attestation objects

License:        Apache-2.0
URL:            https://github.com/trailofbits/pypi-attestations
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pyasn1 >= 0.6
Conflicts:      python%{python3_pkgversion}-pyasn1 >= 0.7
Requires:       python%{python3_pkgversion}-pydantic >= 2.10.0
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-rfc3986
Requires:       python%{python3_pkgversion}-sigstore >= 4.0
Requires:       python%{python3_pkgversion}-sigstore < 5.0
Requires:       python%{python3_pkgversion}-sigstore-models

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.0.28-2
- Bump release for EL10 rebuild

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 0.0.28-1
- Initial package.
