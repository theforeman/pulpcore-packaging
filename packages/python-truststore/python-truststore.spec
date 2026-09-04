%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name truststore

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.10.4
Release:        1%{?dist}
Summary:        Verify certificates using native system trust stores

License:        MIT
URL:            https://github.com/sethmlarson/truststore
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Allow-flit-core-4.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit_core >= 3.11
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
Truststore exposes native system certificate stores through an SSLContext-like
API, allowing applications to use operating-system managed trust roots.


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
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Sep 04 2026 Odilon Sousa <osousa@redhat.com> - 0.10.4-1
- Initial package
