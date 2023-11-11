%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name rich

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        13.3.1
Release:        4%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

License:        None
URL:            https://github.com/Textualize/rich
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-colorama < 0.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-colorama >= 0.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-commonmark < 0.10.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-commonmark >= 0.9.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dataclasses < 0.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dataclasses >= 0.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygments < 3.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygments >= 2.6.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-4
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-3
- Remove typing-extension requirement

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-2
- Disable auto dependency generator

* Fri Feb 03 2023 Odilon Sousa 13.3.1-1
- Update to 13.3.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 10.12.0-3
- Obsolete the old Python 3.9 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 10.12.0-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 10.12.0-1
- Release python-rich 10.12.0

* Wed Oct 20 2021 Evgeni Golov - 10.0.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 10.0.1-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov 10.0.1-1
- Update to 10.0.1

* Thu Nov 05 2020 Evgeni Golov - 6.1.1-2
- Fix License tag in spec file

* Wed Sep 09 2020 Evgeni Golov 6.1.1-1
- Update to 6.1.1

* Tue Sep 01 2020 Evgeni Golov 6.0.0-1
- Update to 6.0.0

* Tue Aug 25 2020 Evgeni Golov - 5.2.1-1
- Initial package.
