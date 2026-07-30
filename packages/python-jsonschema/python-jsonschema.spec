%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name jsonschema

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.10.3
Release:        7%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            https://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli


Requires:       python%{python3_pkgversion}-attrs >= 17.4.0
Requires:       python%{python3_pkgversion}-pyrsistent >= 0.14.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
%exclude %{_bindir}/jsonschema
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 4.10.3-7
- Bump release for EL10 rebuild

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 4.10.3-6
- Add obsoletes for python3.11 package

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 4.10.3-5
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.10.3-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.10.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.10.3-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 4.10.3-1
- Release python-jsonschema 4.10.3

* Wed Sep 28 2022 Odilon Sousa <osousa@redhat.com> - 4.9.1-1
- Release python-jsonschema 4.9.1

* Thu Aug 11 2022 Odilon Sousa <osousa@redhat.com> - 4.6.0-4
- Adding dependencie requirement on python-jsonschema for importlib-resources

* Tue Jul 26 2022 Odilon Sousa <osousa@redhat.com> - 4.6.0-1
- Release python-jsonschema 4.6.0 and add a setup.cfg to build on top of EL7

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-8
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 3.2.0-7
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 3.2.0-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.2.0-5
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.2.0-4
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.0-3
- Bump release to build for el8

* Sun Feb 02 2020 Evgeni Golov - 3.2.0-2
- correct jsonschema requires

* Tue Jan 28 2020 Evgeni Golov - 3.2.0-1
- Initial package.
