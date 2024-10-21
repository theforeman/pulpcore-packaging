%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-auth

Name:           python-%{pypi_name}
Version:        2.35.0
Release:        1%{?dist}
Summary:        Google Authentication Library

License:        Apache 2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_auth-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-cachetools < 6
Requires:       python%{python3_pkgversion}-cachetools >= 2
Requires:       python%{python3_pkgversion}-pyasn1-modules >= 0.2.1
Requires:       python%{python3_pkgversion}-rsa < 5
Requires:       python%{python3_pkgversion}-rsa >= 3.1.4


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n google_auth-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
set -ex
%py3_build



%install
set -ex
%py3_install



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/google_auth-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.35.0-1
- Initial package.