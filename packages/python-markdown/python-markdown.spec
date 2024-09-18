%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name Markdown
%global srcname markdown

Name:           python-%{srcname}
Version:        3.7
Release:        1%{?dist}
Summary:        Python implementation of Markdown

License:        BSD License
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


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
%{python3_sitelib}/%{srcname}
%exclude %{_bindir}/markdown_py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.7-1
- Update to 3.7

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.4.1-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.4.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.4.1-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.4.1-1
- Update to 3.4.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.3.6-3
- Build against python 3.9

* Wed Feb 23 2022 Odilon Sousa <osousa@redhat.com> - 3.3.6-2
- Update dependencies

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 3.3.6-1
- Release python-markdown 3.3.6

* Fri Nov 05 2021 Satoe Imaishi - 3.3.4-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 3.3.4-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 3.3.4-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.3.4-1
- Update to 3.3.4

* Thu Oct 29 2020 Evgeni Golov 3.3.3-1
- Update to 3.3.3

* Tue Jun 23 2020 Evgeni Golov - 3.2.2-1
- Initial package.
