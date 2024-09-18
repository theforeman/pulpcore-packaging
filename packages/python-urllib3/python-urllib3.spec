%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        2.2.3
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
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
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.3-1
- Update to 2.2.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.26.18-3
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.26.18-2
- Rollback overzealous obsoletes

* Mon Nov 27 2023 Odilon Sousa <osousa@redhat.com> - 1.26.18-1
- Release python-urllib3 1.26.18

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.26.8-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.26.8-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.26.8-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 1.26.8-1
- Release python-urllib3 1.26.8

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 1.26.7-1
- Release python-urllib3 1.26.7

* Mon Sep 06 2021 Evgeni Golov - 1.26.6-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 1.26.6-1
- Update to 1.26.6

* Thu Jul 08 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.26.5-1
- Release python-urllib3 1.26.5

* Fri Mar 19 2021 Evgeni Golov 1.26.4-1
- Update to 1.26.4

* Thu Oct 29 2020 Evgeni Golov 1.25.11-1
- Update to 1.25.11

* Mon Aug 10 2020 Evgeni Golov 1.25.10-1
- Update to 1.25.10

* Tue Apr 28 2020 Evgeni Golov 1.25.9-1
- Update to 1.25.9

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.25.8-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 1.25.8-1
- Update to 1.25.8

* Mon Nov 18 2019 Evgeni Golov - 1.25.7-1
- Initial package.
