# Created by pyp2rpm-3.3.3
%global pypi_name pulp-deb

Name:           python-%{pypi_name}
Version:        2.14.1
Release:        2%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-debian >= 0.1.36
Requires:       python%{python3_pkgversion}-pulpcore < 3.16
Requires:       python%{python3_pkgversion}-pulpcore >= 3.14
Requires:       python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(deb) = %{version}

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
%doc README.md
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 19 2021 Evgeni Golov - 2.14.1-2
- Add provides for 'pulpcore-plugin'

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
