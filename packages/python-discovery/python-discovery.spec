%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name python_discovery
%global srcname discovery

Name:           python%{python3_pkgversion}-%{srcname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        A utility to discover Python interpreters

License:        MIT
URL:            https://github.com/tox-dev/python-discovery
Source0:        https://files.pythonhosted.org/packages/source/p/python-discovery/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-filelock >= 3.15.4
Requires:       python%{python3_pkgversion}-platformdirs >= 4.3.6
Requires:       python%{python3_pkgversion}-platformdirs < 5

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

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


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Mar 30 2026 Odilon Sousa <osousa@redhat.com> - 1.2.1-1
- Initial package.
