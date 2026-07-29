%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name Parsley
%global srcname parsley

Name:           python%{python3_pkgversion}-%{srcname}
Version:        1.3
Release:        8%{?dist}
Summary:        Parsing and pattern matching made easy

License:        MIT License
URL:            http://launchpad.net/parsley
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc terml/README.txt
%{python3_sitelib}/__pycache__/parsley.*
%{python3_sitelib}/parsley.py
%{python3_sitelib}/ometa
%{python3_sitelib}/terml
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 1.3-8
- Bump release for EL10 rebuild

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 1.3-7
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.3-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.3-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov - 1.3-1
- Initial package.
