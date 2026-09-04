%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name httpx2

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.12.0
Release:        1%{?dist}
Summary:        Next-generation HTTP client for Python

License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Use-static-version-and-dependency-metadata.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-anyio >= 4.10
Requires:       python%{python3_pkgversion}-httpcore2 >= 2.12
Requires:       python%{python3_pkgversion}-httpcore2 < 2.13
Requires:       python%{python3_pkgversion}-idna >= 3.18
Requires:       python%{python3_pkgversion}-truststore >= 0.10
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.5.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
HTTPX2 is a fully featured synchronous and asynchronous HTTP client with
support for HTTP/1.1 and HTTP/2.


%prep
set -ex
%autosetup -n %{pypi_name}-%{version} -p1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}


%changelog
* Fri Sep 04 2026 Odilon Sousa <osousa@redhat.com> - 2.12.0-1
- Initial package
