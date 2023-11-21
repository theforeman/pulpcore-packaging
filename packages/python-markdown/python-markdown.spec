%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Markdown
%global srcname markdown

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.4.1
Release:        3%{?dist}
Summary:        Python implementation of Markdown

License:        BSD License
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 4.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.md
%exclude %{_bindir}/markdown_py
%{python3_sitelib}/markdown
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
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
