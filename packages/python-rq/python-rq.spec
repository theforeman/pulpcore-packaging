%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name rq

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        7%{?dist}
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them

License:        BSD
URL:            https://github.com/nvie/rq/
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Have-hearbeats-occur-more-frequently.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-click >= 5.0.0
Requires:       python%{python3_pkgversion}-redis >= 3.5.0
Requires:       python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.9.0-7
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.9.0-6
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.9.0-5
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane - 1.9.0-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.9.0-3
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 1.9.0-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 1.9.0-1
- Update to 1.9.0

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
