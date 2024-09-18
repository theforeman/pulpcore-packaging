%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name wcmatch

Name:           python-%{pypi_name}
Version:        9.0
Release:        1%{?dist}
Summary:        Wildcard/glob file name matcher

License:        MIT License
URL:            https://github.com/facelessuser/wcmatch
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-bracex >= 2.1.1


%description -n python%{python3_pkgversion}-%{pypi_name}
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
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 9.0-1
- Update to 9.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 8.3-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 8.3-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 8.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 8.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 8.3-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 8.3-1
- Update to 8.3

* Wed Sep 08 2021 Evgeni Golov - 8.2-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 8.2-1
- Update to 8.2

* Wed Mar 31 2021 Evgeni Golov - 8.1.2-1
- Initial package.
