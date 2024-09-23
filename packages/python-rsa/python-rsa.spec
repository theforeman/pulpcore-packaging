%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name rsa

Name:           python-%{pypi_name}
Version:        4.9
Release:        1%{?dist}
Summary:        Pure-Python RSA implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/sybrenstuvel/python-rsa/
Source:         https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyasn1 >= 0.1.3

%description -n python%{python3_pkgversion}-%{pypi_name}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/pyrsa-decrypt
%{_bindir}/pyrsa-encrypt
%{_bindir}/pyrsa-keygen
%{_bindir}/pyrsa-priv2pub
%{_bindir}/pyrsa-sign
%{_bindir}/pyrsa-verify

%changelog
* Mon Sep 23 2024 Odilon Sousa - 4.9-1
- Initial package.