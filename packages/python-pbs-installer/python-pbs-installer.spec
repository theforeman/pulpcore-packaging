%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name pbs-installer
%global srcname pbs_installer

Name:           python%{python3_pkgversion}-%{srcname}
Version:        2025.11.20
Release:        1%{?dist}
Summary:        Installer for Python Build Standalone
BuildArch:      noarch

License:        MIT
URL:            https://github.com/frostming/pbs-installer
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-pdm-backend
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%package -n python%{python3_pkgversion}-%{srcname}+install
Summary: Metapackage for python%{python3_pkgversion}-%{srcname}: install extra
Requires: python%{python3_pkgversion}-zstandard >= 0.21.0

%description -n python%{python3_pkgversion}-%{srcname}+install
This is a metapackage bringing in install extra requires for python%{python3_pkgversion}-%{srcname}
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{srcname}+install
%ghost %{python3_sitelib}/%{srcname}-%{version}.dist-info/

%package -n python%{python3_pkgversion}-%{srcname}+download
Summary: Metapackage for python%{python3_pkgversion}-%{srcname}: download extra
Requires: python%{python3_pkgversion}-httpx >= 0.27.0
Requires: python%{python3_pkgversion}-httpx < 1

%description -n python%{python3_pkgversion}-%{srcname}+download
This is a metapackage bringing in install extra requires for python%{python3_pkgversion}-%{srcname}
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{srcname}+download
%ghost %{python3_sitelib}/%{srcname}-%{version}.dist-info/


%prep
set -ex
%autosetup -n %{srcname}-%{version}

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%exclude %{_bindir}/pbs-install


%changelog
* Sun Nov 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.11.20-1
- Update to 2025.11.20

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.10.31-1
- Update to 2025.10.31

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.10.14-1
- Update to 2025.10.14

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 2025.2.12-2
- Rebuild against python3.12

* Mon Mar 10 2025 Odilon Sousa - 2025.2.12-1
- Initial package.
