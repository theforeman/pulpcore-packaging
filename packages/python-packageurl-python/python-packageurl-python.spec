%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name packageurl-python
%global srcname packageurl_python

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.17.6
Release:        1%{?dist}
Summary:        Package URL parser and builder for Python
License:        MIT
URL:            https://github.com/package-url/packageurl-python
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%description
A parser and builder for Package URLs (purl).

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license mit.LICENSE
%doc README.rst
%{python3_sitelib}/packageurl/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
* Tue Nov 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.17.6-1
- Add packageurl-python required by python-sbom
