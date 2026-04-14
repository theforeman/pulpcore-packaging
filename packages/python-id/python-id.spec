%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name id

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.6.1
Release:        1%{?dist}
Summary:        A library for generating OIDC identities

License:        Apache-2.0
URL:            https://github.com/di/id
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit-core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-urllib3 >= 2
Requires:       python%{python3_pkgversion}-urllib3 < 3

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 1.6.1-1
- Initial package.
