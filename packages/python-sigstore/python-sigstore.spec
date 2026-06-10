%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name sigstore

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.3.0
Release:        1%{?dist}
Summary:        A tool for signing and verifying Python package distributions

License:        Apache-2.0
URL:            https://github.com/sigstore/sigstore-python
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit-core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-cryptography >= 42
Requires:       python%{python3_pkgversion}-cryptography < 49
Requires:       python%{python3_pkgversion}-id >= 1.1.0
Requires:       python%{python3_pkgversion}-pyasn1 >= 0.6
Conflicts:      python%{python3_pkgversion}-pyasn1 >= 0.7
Requires:       python%{python3_pkgversion}-pydantic >= 2
Conflicts:      python%{python3_pkgversion}-pydantic >= 3
Requires:       python%{python3_pkgversion}-pyjwt >= 2.1
Requires:       python%{python3_pkgversion}-pyOpenSSL >= 23.0.0
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-rich >= 13
Requires:       python%{python3_pkgversion}-rich < 16
Requires:       python%{python3_pkgversion}-rfc8785 >= 0.1.2
Conflicts:      python%{python3_pkgversion}-rfc8785 >= 0.2
Requires:       python%{python3_pkgversion}-rfc3161-client >= 1.0.3
Requires:       python%{python3_pkgversion}-rfc3161-client < 1.1.0
Requires:       python%{python3_pkgversion}-sigstore-models == 0.0.6
Requires:       python%{python3_pkgversion}-sigstore-rekor-types == 0.0.18
Requires:       python%{python3_pkgversion}-tuf >= 6.0
Conflicts:      python%{python3_pkgversion}-tuf >= 8.0
Requires:       python%{python3_pkgversion}-platformdirs >= 4.2
Conflicts:      python%{python3_pkgversion}-platformdirs >= 5.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}


%changelog
* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.3.0-1
- Update to 4.3.0
- Update cryptography bound to < 49, tuf Conflicts to >= 8.0, rich bound to < 16

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 4.2.0-1
- Initial package.
