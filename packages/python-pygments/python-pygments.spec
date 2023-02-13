%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%global debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name Pygments
%global srcname pygments

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.14.0
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python

License:        BSD
URL:            https://pygments.org/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

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
%license LICENSE
%doc README.rst
%exclude %{_bindir}/pygmentize
%{python3_sitelib}/pygments
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
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
