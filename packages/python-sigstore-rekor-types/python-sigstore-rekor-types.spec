%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name sigstore-rekor-types
%global src_name sigstore_rekor_types

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.0.18
Release:        1%{?dist}
Summary:        Pydantic types for Sigstore Rekor

License:        Apache-2.0
URL:            https://trailofbits.github.io/sigstore-rekor-types/
Source0:        https://files.pythonhosted.org/packages/source/s/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-pydantic >= 2
Conflicts:      python%{python3_pkgversion}-pydantic >= 3
Requires:       python%{python3_pkgversion}-email-validator

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Replace pydantic[email] extra with plain pydantic (email-validator added explicitly)
sed -i "s/pydantic\[email\]/pydantic/" pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitelib}/rekor_types
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Wed Apr 15 2026 Odilon Sousa <osousa@redhat.com> - 0.0.18-1
- Initial package.
- Add email-validator Requires (pydantic[email] extra); strip extra from pyproject.toml
