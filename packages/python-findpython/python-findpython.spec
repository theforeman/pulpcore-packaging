%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name findpython

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.7.1
Release:        1%{?dist}
Summary:        A utility to find python versions on your system
BuildArch:      noarch

License:        MIT
URL:            https://github.com/frostming/findpython
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-pdm-backend
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:  python%{python3_pkgversion}-packaging

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.1-1
- Update to 0.7.1

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.0-1
- Update to 0.7.0

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 0.6.3-2
- Rebuild against python3.12

* Mon Mar 10 2025 Odilon Sousa - 0.6.3-1
- Initial package.
