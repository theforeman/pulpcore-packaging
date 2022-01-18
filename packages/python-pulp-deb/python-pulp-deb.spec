%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-deb

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.16.0
Release:        1%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-debian >= 0.1.36
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.18
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.15
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-debian >= 0.1.36
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.18
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.15
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 2.16.0-1
- Update to 2.16.0

* Thu Jan 13 2022 Quirin Pamp - 2.16.1-1
- Update to 2.16.1

* Thu Nov 11 2021 Quirin Pamp - 2.16.0-1
- Update to 2.16.0

* Mon Oct 18 2021 Evgeni Golov - 2.15.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Wed Sep 08 2021 Evgeni Golov 2.15.0-1
- Update to 2.15.0

* Mon Aug 02 2021 Quirin Pamp 2.14.1-1
- Update to 2.14.1

* Fri Jun 11 2021 Evgeni Golov 2.13.0-1
- Update to 2.13.0

* Tue May 25 2021 Quirin Pamp 2.11.2-1
- Update to 2.11.2

* Thu Apr 15 2021 Quirin Pamp 2.11.1-1
- Update to 2.11.1

* Fri Mar 19 2021 Evgeni Golov 2.10.0-1
- Update to 2.10.0

* Mon Jan 11 2021 Evgeni Golov 2.8.0-1
- Update to 2.8.0

* Wed Sep 30 2020 Evgeni Golov - 2.7.0-1
- Release python-pulp-deb 2.7.0

* Thu Sep 03 2020 Evgeni Golov 2.6.1-1
- Update to 2.6.1

* Thu Jun 18 2020 Evgeni Golov - 2.4.0-0.1.b1
- Update to 2.4.0b1

* Thu Apr 30 2020 ATIX AG <info@atix.de> - 2.3.0-0.1.b1
- Initial package.
