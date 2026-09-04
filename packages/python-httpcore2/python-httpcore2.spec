%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name httpcore2

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.12.0
Release:        1%{?dist}
Summary:        Minimal low-level HTTP client

License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Use-static-version-metadata.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-h11 >= 0.16
Requires:       python%{python3_pkgversion}-truststore >= 0.10

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
HTTP Core 2 provides the minimal low-level transport implementation used by
HTTPX2, with synchronous and asynchronous connection pooling.


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


%changelog
* Fri Sep 04 2026 Odilon Sousa <osousa@redhat.com> - 2.12.0-1
- Initial package
