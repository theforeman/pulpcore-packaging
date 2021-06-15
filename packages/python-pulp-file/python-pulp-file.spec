# Created by pyp2rpm-3.3.3
%global pypi_name pulp-file

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1%{?dist}
Summary:        File plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
A Pulp plugin to support hosting arbitrary files.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pulpcore < 3.14
Requires:       python%{python3_pkgversion}-pulpcore >= 3.12
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
A Pulp plugin to support hosting arbitrary files.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_file
%{python3_sitelib}/pulp_file-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 11 2021 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Fri Mar 19 2021 Evgeni Golov 1.6.0-1
- Update to 1.6.0

* Mon Jan 11 2021 Evgeni Golov 1.5.0-1
- Update to 1.5.0

* Mon Sep 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Tue Aug 25 2020 Evgeni Golov 1.2.0-1
- Update to 1.2.0

* Thu Jun 04 2020 Evgeni Golov 1.0.1-1
- Update to 1.0.1

* Tue Apr 28 2020 Evgeni Golov 0.3.0-1
- Update to 0.3.0

* Wed Mar 18 2020 Samir Jha 0.2.0-1
- Update to 0.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.1-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 0.1.1-1
- Update to 0.1.1

* Fri Dec 13 2019 Evgeni Golov 0.1.0-1
- Update to 0.1.0

* Mon Nov 18 2019 Evgeni Golov - 0.1.0rc1-1
- Initial package.
