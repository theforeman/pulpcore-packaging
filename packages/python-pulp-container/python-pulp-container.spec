# Created by pyp2rpm-3.3.3
%global pypi_name pulp-container

Name:           python-%{pypi_name}
Version:        2.7.0
Release:        1%{?dist}
Summary:        Container plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-ecdsa >= 0.13.2
Conflicts:      python%{python3_pkgversion}-ecdsa >= 0.14
Requires:       python%{python3_pkgversion}-pyjwkest >= 1.4.0
Conflicts:      python%{python3_pkgversion}-pyjwkest >= 1.5
Requires:       python%{python3_pkgversion}-pyjwt >= 1.7.1
Conflicts:      python%{python3_pkgversion}-pyjwt >= 1.8
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-url-normalize >= 1.4.2
Conflicts:      python%{python3_pkgversion}-url-normalize >= 1.5

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-ecdsa >= 0.13.2
Conflicts:      python%{python3_pkgversion}-ecdsa >= 0.14
Requires:       python%{python3_pkgversion}-pulpcore < 3.15
Requires:       python%{python3_pkgversion}-pulpcore >= 3.14
Requires:       python%{python3_pkgversion}-pyjwkest >= 1.4.0
Conflicts:      python%{python3_pkgversion}-pyjwkest >= 1.5
Requires:       python%{python3_pkgversion}-pyjwt >= 1.7.1
Conflicts:      python%{python3_pkgversion}-pyjwt >= 1.8
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-url-normalize >= 1.4.2
Conflicts:      python%{python3_pkgversion}-url-normalize >= 1.5

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

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
%{python3_sitelib}/pulp_container
%{python3_sitelib}/pulp_container-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 02 2021 Evgeni Golov - 2.7.0-1
- Release python-pulp-container 2.7.0

* Fri Jun 11 2021 Evgeni Golov 2.6.0-1
- Update to 2.6.0

* Mon May 31 2021 Evgeni Golov - 2.5.3-1
- Release python-pulp-container 2.5.3

* Wed May 05 2021 Justin Sherrill <jsherril@redhat.com> 2.5.2-2
- add patch for issue 8672

* Mon Apr 26 2021 Evgeni Golov - 2.5.2-1
- Release python-pulp-container 2.5.2

* Mon Apr 19 2021 Evgeni Golov - 2.5.1-1
- Release python-pulp-container 2.5.1

* Tue Apr 13 2021 Evgeni Golov - 2.5.0-1
- Release python-pulp-container 2.5.0

* Fri Mar 19 2021 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Mon Jan 11 2021 Evgeni Golov 2.2.0-1
- Update to 2.2.0

* Mon Sep 28 2020 Evgeni Golov 2.1.0-1
- Update to 2.1.0

* Tue Sep 08 2020 Justin Sherrill <jsherril@redhat.com> 2.0.1-1
- update to 2.0.1

* Tue Aug 25 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Fri Jul 17 2020 Justin Sherrill <jsherril@redhat.com> 1.4.2-1
- upgrade to 1.4.2

* Thu Jun 04 2020 Evgeni Golov 1.4.1-1
- Update to 1.4.1

* Tue Apr 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Wed Mar 18 2020 Samir Jha 1.2.0-1
- Update to 1.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.0.0-1
- Update to 1.0.0

* Tue Nov 19 2019 Evgeni Golov - 1.0.0rc1-1
- Initial package.
