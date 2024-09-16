%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name Pygments
%global srcname pygments

Name:           python-%{srcname}
Version:        2.18.0
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python

License:        BSD
URL:            https://pygments.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{srcname}
%exclude %{_bindir}/pygmentize
%{python3_sitelib}/pygments
%{python3_sitelib}/%{srcname}-%{version}.dist-info/


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.18.0-1
- Update to 2.18.0

* Fri Mar 01 2024 Odilon Sousa <osousa@redhat.com> - 2.17.0-1
- Release python-pygments 2.17.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.14.0-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.14.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.14.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2.14.0-1
- Update to 2.14.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.11.2-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 2.11.2-1
- Release python-pygments 2.11.2

* Thu Nov 25 2021 Odilon Sousa <osousa@redhat.com> - 2.10.0-2
- Release python-pygments 2.10.0

* Fri Nov 05 2021 Satoe Imaishi - 2.8.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 2.8.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.8.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.8.1-1
- Update to 2.8.1

* Thu Oct 29 2020 Evgeni Golov 2.7.2-1
- Update to 2.7.2

* Tue Aug 25 2020 Evgeni Golov - 2.6.1-1
- Initial package.
