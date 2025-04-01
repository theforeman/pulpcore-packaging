%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name requirements-parser

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.2.0
Release:        8%{?dist}
Summary:        Parses Pip requirement files

License:        BSD
URL:            https://github.com/davidfischer/requirements-parser
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/requirements
%{python3_sitelib}/requirements_parser-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 0.2.0-8
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.2.0-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.2.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.2.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.2.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.2.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.2.0-2
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.2.0-1
- Initial package.
