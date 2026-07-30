%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name sigstore-models
%global src_name sigstore_models

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.0.6
Release:        2%{?dist}
Summary:        Data models for Sigstore

License:        Apache-2.0
URL:            https://github.com/sigstore/sigstore-python
Source0:        https://files.pythonhosted.org/packages/source/s/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-uv-build
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-pydantic >= 2.12
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.14.1

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.0.6-2
- Bump release for EL10 rebuild

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 0.0.6-1
- Initial package.
