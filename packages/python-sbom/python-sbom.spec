%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name python-sbom
%global srcname python_sbom

Name:           python%{python3_pkgversion}-sbom
Version:        0.3.1
Release:        1%{?dist}
Summary:        Generate Python package software bills of materials
License:        MIT AND Apache-2.0
URL:            https://github.com/tox-dev/python-sbom
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-packaging >= 26.3
BuildRequires:  python%{python3_pkgversion}-hatchling >= 1.32.4
BuildRequires:  python%{python3_pkgversion}-hatch_vcs >= 0.5
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme >= 25.1
BuildRequires:  python%{python3_pkgversion}-installer >= 1.1
BuildRequires:  python%{python3_pkgversion}-packageurl-python >= 0.11.1
BuildRequires:  python%{python3_pkgversion}-zipremove >= 0.10
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-installer >= 1.1
Requires:       python%{python3_pkgversion}-packageurl-python >= 0.11.1
Requires:       python%{python3_pkgversion}-packaging >= 26.3
Requires:       python%{python3_pkgversion}-zipremove >= 0.10
Requires:       python%{python3_pkgversion}-hatchling >= 1.28

%description
Python package SBOM support, including a Hatchling build hook.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{_bindir}/python-sbom

%changelog
* Tue Nov 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.1-1
- Add python-sbom Hatchling build hook for filelock
