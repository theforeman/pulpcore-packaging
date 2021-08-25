# Created by pyp2rpm-3.3.3
%global pypi_name pulp-2to3-migration

# We use a wrong source RPM name here, as the original one triggers a bug in tito
# See https://github.com/dgoodwin/tito/pull/333
Name:           python-pulp_2to3_migration
Version:        0.11.3
Release:        1%{?dist}
Summary:        Pulp 2 to Pulp 3 migration tool

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-jsonschema >= 3.0
Requires:       python3-mongoengine
Requires:       python3-pulpcore < 3.13
Requires:       python3-pulpcore >= 3.6
Requires:       python3-semantic-version
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pulp_2to3_migration
%{python3_sitelib}/pulp_2to3_migration-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 25 2021 Evgeni Golov - 0.11.3-1
- Release python-pulp_2to3_migration 0.11.3

* Mon Jun 14 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.11.2-1
- Update to 0.11.2

* Mon May 24 2021 Justin Sherrill <jsherril@redhat.com> 0.11.1-1
- update to 0.11.1

* Tue Apr 13 2021 Evgeni Golov - 0.11.0-1
- Release python-pulp_2to3_migration 0.11.0

* Wed Mar 24 2021 Evgeni Golov - 0.10.0-1
- Release python-pulp_2to3_migration 0.10.0

* Thu Mar 11 2021 Justin Sherrill <jsherril@redhat.com> 0.9.1-1
- update to 0.9.1

* Wed Mar 10 2021 Evgeni Golov - 0.9.0-1
- Release python-pulp_2to3_migration 0.9.0

* Thu Feb 18 2021 Justin Sherrill <jsherril@redhat.com> 0.8.0-1
- update to 0.8.0

* Thu Feb 11 2021 Justin Sherrill <jsherril@redhat.com> 0.7.0-1
- upgrade to 0.7.0

* Tue Jan 19 2021 Evgeni Golov 0.6.0-2
- correct pulpcore version constraint -- 3.9 is supported

* Wed Dec 09 2020 Justin Sherrill <jsherril@redhat.com> 0.6.0-1
- update to 0.6.0

* Tue Oct 27 2020 Justin Sherrill <jsherril@redhat.com> 0.5.1-1
- update to 0.5.1

* Thu Oct 15 2020 Justin Sherrill <jsherril@redhat.com> 0.5.0-1
- bump to 0.5.0

* Thu Oct 08 2020 Evgeni Golov - 0.4.0-1
- Release python-pulp_2to3_migration 0.4.0

* Fri Aug 28 2020 Evgeni Golov - 0.3.0-1
- Update to 0.3.0

* Mon Aug 03 2020 Evgeni Golov - 0.2.0-0.1.b7
- Update to 0.2.0-b7

* Wed Jun 17 2020 Justin Sherrill <jsherril@redhat.com> 0.2.0-0.1.b3
- updated to 0.2.0b3

* Wed Apr 29 2020 Evgeni Golov - 0.2.0-0.1.b2
- Update to 0.2.0-b2

* Wed Mar 25 2020 Samir Jha <sjha4@ncsu.edu> - 0.2.0-0.1.b1
- Update to 0.2.0-b1

* Tue Mar 03 2020 Evgeni Golov - 0.1.0-0.1.rc1
- Update to 0.1.0-rc1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.0.1-0.2.rc1
- Bump release to build for el8

* Wed Feb 19 2020 Evgeni Golov - 0.0.1-0.1.rc1
- Update to 0.0.1-rc1

* Tue Jan 28 2020 Evgeni Golov - 0.0.1-0.1.beta1
- Initial package.
