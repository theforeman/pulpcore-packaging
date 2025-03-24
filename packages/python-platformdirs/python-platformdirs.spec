%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name platformdirs

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.3.6
Release:        2%{?dist}
Summary:        A small Python module for determining appropriate platform-specific dirs, e

License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli

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

%changelog
* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 4.3.6-2
- Rebuild against python3.12

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.3.6-1
- Update to 4.3.6

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.10.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.10.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.10.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-2
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-1
- Release python-platformdirs 3.10.0

* Mon Jul 24 2023 Odilon Sousa <osousa@redhat.com> - 2.6.2-1
- Initial package.
