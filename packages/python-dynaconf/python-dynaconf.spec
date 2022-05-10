%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name dynaconf

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.1.7
Release:        4%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 38.6.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.1.7-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.1.7-3
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 3.1.7-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 13 2021 Evgeni Golov 3.1.7-1
- Update to 3.1.7

* Fri Sep 10 2021 Evgeni Golov - 3.1.5-3
- Don't require typing, our Python is new enough

* Mon Sep 06 2021 Evgeni Golov - 3.1.5-2
- Build against Python 3.8

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.1.5-1
- Release python-dynaconf 3.1.5

* Fri Mar 19 2021 Evgeni Golov 3.1.4-1
- Update to 3.1.4

* Thu Oct 29 2020 Evgeni Golov 3.1.2-1
- Update to 3.1.2

* Mon Sep 28 2020 Evgeni Golov 3.1.1-1
- Update to 3.1.1

* Tue Aug 25 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Wed Mar 18 2020 Samir Jha 3.0.0-0.1.rc1
- Update to 3.0.0rc1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.2.2-1
- Update to 2.2.2

* Fri Dec 13 2019 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
