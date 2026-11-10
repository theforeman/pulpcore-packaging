%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name zipremove

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Remove members from Python ZIP archives
License:        MIT
URL:            https://github.com/danny0838/zipremove
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%description
Utilities for removing entries from ZIP files.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Nov 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.0-1
- Add zipremove required by python-sbom
- Ensure pyproject file processing has Python packaging on EL9
