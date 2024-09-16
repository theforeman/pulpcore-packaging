%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

%global debug_package %{nil}
# Created by pyp2rpm-3.3.3
%global pypi_name PyYAML
%global srcname pyyaml

Name:           python-%{srcname}
Version:        6.0.1
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://pyyaml.org/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildRequires:  gcc
BuildRequires:  libyaml-devel


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-yaml}
Provides:       python%{python3_pkgversion}-yaml = %{version}-%{release}


%description -n python%{python3_pkgversion}-%{srcname}
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


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%{python3_sitearch}/_yaml
%{python3_sitearch}/yaml
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.0.1-1
- Update to 6.0.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 5.4.1-8
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 5.4.1-7
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 5.4.1-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.4.1-5
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.4.1-4
- Build against python 3.9

* Wed Sep 22 2021 Evgeni Golov - 5.4.1-3
- Correct provides for Python 3.8

* Wed Sep 08 2021 Evgeni Golov - 5.4.1-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 5.4.1-1
- Update to 5.4.1

* Tue Jan  5 2021 Evgeni Golov - 5.3.1-3
- Also provide 'yaml' name

* Tue Aug 25 2020 Evgeni Golov - 5.3.1-2
- Provide PyYAML name too

* Tue Apr 14 2020 Evgeni Golov 5.3.1-1
- Update to 5.3.1

* Wed Mar 18 2020 Samir Jha 5.3-1
- Update to 5.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 5.2-1
- Update to 5.2

* Mon Nov 18 2019 Evgeni Golov - 5.1.2-1
- Initial package.
