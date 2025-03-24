%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name webencodings

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.5.1
Release:        8%{?dist}
Summary:        Character encoding aliases for legacy web content

License:        BSD
URL:            https://github.com/SimonSapin/python-webencodings
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 0.5.1-8
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.5.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.5.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.5.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.5.1-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.5.1-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.5.1-2
- Build against Python 3.8

* Tue Jun 23 2020 Evgeni Golov - 0.5.1-1
- Initial package.
