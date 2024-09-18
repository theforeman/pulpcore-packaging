%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name filelock

Name:           python-%{pypi_name}
Version:        3.16.1
Release:        1%{?dist}
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/benediktschmitt/py-filelock
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.16.1-1
- Update to 3.16.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.8.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.8.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.8.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.8.0-2
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.8.0-1
- Release python-filelock 3.8.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.0.12-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.0.12-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 3.0.12-1
- Initial package.
