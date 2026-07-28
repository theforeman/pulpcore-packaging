%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name black

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        24.10.0
Release:        2%{?dist}
Summary:        The uncompromising code formatter

License:        MIT
URL:            https://github.com/psf/black
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling >= 1.20.0
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-click >= 8.0.0
Requires:       python%{python3_pkgversion}-mypy-extensions >= 0.4.3
Requires:       python%{python3_pkgversion}-packaging >= 22.0
Requires:       python%{python3_pkgversion}-pathspec >= 0.9.0
Requires:       python%{python3_pkgversion}-platformdirs >= 2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%package -n python%{python3_pkgversion}-blackd
Summary:        Black HTTP server component
Requires:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-aiohttp >= 3.10

%description -n python%{python3_pkgversion}-blackd
HTTP server for the Black code formatter.


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
%doc README.md
%exclude %{_bindir}/black
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/blib2to3
%{python3_sitelib}/__pycache__/_black_version.*
%{python3_sitelib}/_black_version.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%files -n python%{python3_pkgversion}-blackd
%exclude %{_bindir}/blackd
%{python3_sitelib}/blackd


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 24.10.0-2
- Bump release for EL10 rebuild

* Fri Jun 12 2026 Odilon Sousa <osousa@redhat.com> - 24.10.0-1
- Initial package
