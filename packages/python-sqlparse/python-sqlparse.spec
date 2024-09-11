%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name sqlparse

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        A non-validating SQL parser

License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires: /usr/bin/pathfix.py



%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
#Fix cli.py ambiguous python shebang
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" sqlparse/cli.py


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%exclude %{_bindir}/sqlformat


%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.1-1
- Update to 0.5.1

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 0.5.0-1
- Release python-sqlparse 0.5.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.4.4-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.4-2
- Build against python 3.11

* Mon Jun 12 2023 Odilon Sousa <osousa@redhat.com> - 0.4.4-1
- Release python-sqlparse 0.4.4
- Add setup.cfg and setup.py to build package on EL8

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-3
- Build against python 3.9

* Mon Nov 29 2021 Odilon Sousa <osousa@redhat.com> - 0.4.2-2
- Release python-sqlparse 0.4.2

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.4.2-1
- Release python-sqlparse 0.4.2

* Fri Nov 05 2021 Satoe Imaishi - 0.4.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 0.4.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.4.1-2
- Build against Python 3.8

* Thu Oct 29 2020 Evgeni Golov 0.4.1-1
- Update to 0.4.1

* Wed Mar 18 2020 Samir Jha 0.3.1-1
- Update to 0.3.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.3.0-1
- Initial package.
