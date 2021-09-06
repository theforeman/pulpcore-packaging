%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name rq

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.8.1
Release:        2%{?dist}
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them

License:        BSD
URL:            https://github.com/nvie/rq/
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Have-hearbeats-occur-more-frequently.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click >= 5.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-redis >= 3.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
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
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 1.8.1-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 1.8.1-1
- Update to 1.8.1

* Wed Mar 03 2021 Brian Bouterse - 1.7.0-2
- Have heartbeats occur more frequently within the worker TTL

* Mon Jan 11 2021 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Thu Sep 10 2020 Evgeni Golov 1.5.2-1
- Update to 1.5.2

* Mon Jul 20 2020 Evgeni Golov 1.4.3-1
- Update to 1.4.3

* Thu Jun 04 2020 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Tue Apr 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Wed Mar 18 2020 Samir Jha 1.2.2-1
- Update to 1.2.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.0-1
- Initial package.
