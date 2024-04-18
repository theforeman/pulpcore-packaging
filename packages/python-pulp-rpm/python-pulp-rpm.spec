%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm

Name:           python-%{pypi_name}
Version:        3.25.3
Release:        1%{?dist}
Summary:        RPM plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if 0%{?rhel} == 7
Requires:       libmodulemd2 >= 2.12
%else
Requires:       libmodulemd >= 2.12
%endif
Requires:       python%{python3_pkgversion}-aiohttp-xmlrpc >= 1.5.0
Requires:       python%{python3_pkgversion}-createrepo_c >= 1.0.1
Conflicts:      python%{python3_pkgversion}-createrepo_c >= 1.1.0
Requires:       python%{python3_pkgversion}-django-readonly-field >= 1.1.1
Requires:       python%{python3_pkgversion}-jsonschema >= 4.6
Conflicts:      python%{python3_pkgversion}-jsonschema >= 5.0
Requires:       python%{python3_pkgversion}-libcomps >= 0.1.15
Conflicts:      python%{python3_pkgversion}-libcomps >= 0.2
Requires:       python%{python3_pkgversion}-productmd >= 1.33
Conflicts:      python%{python3_pkgversion}-productmd >= 1.34
Requires:       python%{python3_pkgversion}-pulpcore < 3.55
Requires:       python%{python3_pkgversion}-pulpcore >= 3.44.1
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-solv >= 0.7.21
Conflicts:      python%{python3_pkgversion}-solv >= 0.8

Provides:       pulpcore-plugin(rpm) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove "solv" dependency from setup.py as python3-solv does not provide an egg
sed -i "/solv/d" requirements.txt


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_rpm
%{python3_sitelib}/pulp_rpm-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Apr 18 2024 Samir Jha <samirjha1525@gmail.com> - 3.25.3-1
- Release python-pulp-rpm 3.25.3

* Wed Apr 03 2024 Samir Jha <samirjha1525@gmail.com> - 3.25.2-1
- Release python-pulp-rpm 3.25.2

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.25.1-1
- Release python-pulp-rpm 3.25.1

* Wed Mar 06 2024 Odilon Sousa <osousa@redhat.com> - 3.23.3-1
- Release python-pulp-rpm 3.23.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.23.0-3
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.23.0-2
- Obsolete python39 packages for a smooth upgrade

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 3.23.0-1
- Release python-pulp-rpm 3.23.0

* Wed Oct 18 2023 Odilon Sousa <osousa@redhat.com> - 3.22.6-1
- Release python-pulp-rpm 3.22.6

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 3.22.3-1
- Release python-pulp-rpm 3.22.3

* Mon Mar 20 2023 Odilon Sousa <osousa@redhat.com> - 3.19.2-1
- Release python-pulp-rpm 3.19.2

* Wed Mar 01 2023 Odilon Sousa <osousa@redhat.com> - 3.19.0-3
- Remove PyGObject requirement, it was dropped with 3.19.0 release

* Thu Feb 16 2023 Odilon Sousa <osousa@redhat.com> - 3.19.0-2
- Update requiriments for jsonschema

* Wed Feb 15 2023 Ian Ballou <ianballou67@gmail.com> - 3.19.0-1
- Release python-pulp-rpm 3.19.0

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.18.10-1
- Release python-pulp-rpm 3.18.10

* Tue Nov 29 2022 Ian Ballou <ianballou67@gmail.com> - 3.18.9-1
- Release python-pulp-rpm 3.18.9

* Wed Oct 12 2022 Patrick Creech <pcreech@redhat.com> - 3.18.7-1
- Release python-pulp-rpm 3.18.7

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-1
- Release python-pulp-rpm 3.18.5

* Tue Sep 20 2022 Odilon Sousa 3.18.1-1
- Update to 3.18.1

* Mon Sep 05 2022 Odilon Sousa <osousa@redhat.com> - 3.17.10-3
- Bump release for a better upgrade from pulpcore 3.16

* Mon Sep 05 2022 Odilon Sousa <osousa@redhat.com> - 3.17.10-2
- Bump release to rebuild on top of python 3.8

* Wed Aug 31 2022 Patrick Creech <pcreech@redhat.com> - 3.17.10-1
- Release python-pulp-rpm 3.17.10

* Thu Aug 11 2022 Odilon Sousa <osousa@redhat.com> - 3.17.7-3
- Update release for better upgrade from 3.16 to 3.18

* Tue Jul 26 2022 Odilon Sousa <osousa@redhat.com> - 3.17.7-1
- Release python-pulp-rpm 3.17.7

* Mon May 30 2022 Odilon Sousa <osousa@redhat.com> - 3.17.5-3
- Bumpining release to rebuild against python 3.9

* Wed May 25 2022 Odilon Sousa <osousa@redhat.com> - 3.17.5-2
- Bump release to rebuild against python 3.9

* Tue May 10 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.17.5-1
- Release python-pulp-rpm 3.17.5

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.4-3
- Obsolete the old Python 3.9 package for smooth upgrade

* Mon May 09 2022 Odilon Sousa <osousa@redhat.com> - 3.17.4-2
- Adding a conditional for Python Gobject we will use the package from EL9 repos
  on EL9 systems

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 3.17.4-1
- Release python-pulp-rpm 3.17.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.3-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.17.3-1
- Release python-pulp-rpm 3.17.3

* Mon Nov 29 2021 Justin Sherrill <jsherril@redhat.com> 3.16.1-2
- require libmodulemd for rhel 9

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 3.16.1-1
- Release python-pulp-rpm 3.16.1

* Mon Oct 18 2021 Evgeni Golov - 3.15.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 3.15.0-1
- Update to 3.15.0

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.14.2-1
- Release python-pulp-rpm 3.14.2

* Mon Aug 23 2021 Justin Sherrill <jsherril@redhat.com> 3.14.1-1
- update to 3.14.1

* Mon Jul 26 2021 Justin Sherrill <jsherril@redhat.com> 3.14.0-1
- update to 3.14.0

* Wed Jul 07 2021 Justin Sherrill <jsherril@redhat.com> 3.13.3-1
- upgrade to 3.13.3

* Tue Jun 29 2021 Evgeni Golov - 3.13.2-1
- Release python-pulp-rpm 3.13.2

* Wed Jun 16 2021 Evgeni Golov 3.12.0-2
- Depend on aiohttp-xmlrpc

* Fri Jun 11 2021 Evgeni Golov 3.12.0-1
- Update to 3.12.0

* Wed May 19 2021 Evgeni Golov - 3.11.0-1
- Release python-pulp-rpm 3.11.0

* Thu Apr 08 2021 Ian Ballou <ianballou67@gmail.com> 3.10.0-1
- Update to 3.10.0

* Fri Mar 19 2021 Evgeni Golov 3.9.1-1
- Update to 3.9.1

* Thu Mar 11 2021 Justin Sherrill <jsherril@redhat.com> 3.9.0-2
- add patch for issue 8245

* Thu Feb 18 2021 Justin Sherrill <jsherril@redhat.com> 3.9.0-1
- update to 3.9.0

* Mon Jan 11 2021 Evgeni Golov 3.8.0-1
- Update to 3.8.0

* Mon Sep 28 2020 Evgeni Golov 3.7.0-1
- Update to 3.7.0

* Mon Sep 07 2020 Evgeni Golov 3.6.2-1
- Update to 3.6.2

* Tue Aug 25 2020 Evgeni Golov 3.6.1-1
- Update to 3.6.1

* Thu Aug 13 2020 Justin Sherrill <jsherril@redhat.com> 3.5.1-1
- update to 3.5.1

* Fri Aug 07 2020 Justin Sherrill <jsherril@redhat.com> 3.5.0-3
- Add patch for issue 7284

* Tue Aug 04 2020 Justin Sherrill <jsherril@redhat.com> 3.5.0-2
- add patch for pulp issue 7248

* Thu Jul 30 2020 Samir Jha 3.5.0-1
- Update to 3.5.0

* Tue Jun 09 2020 Justin Sherrill <jsherril@redhat.com> 3.4.1-2
- solv dep moved to requirements.txt

* Thu Jun 04 2020 Evgeni Golov 3.4.1-1
- Update to 3.4.1

* Thu Jun 04 2020 Evgeni Golov - 3.3.1-5
- Make libmodulemd dependency versioned

* Thu Jun 04 2020 Evgeni Golov <evgeni@golov.de> - 3.3.1-4
- Bump libcomps require to get a version with egg info

* Wed Jun 03 2020 Evgeni Golov - 3.3.1-3
- Add Requires on libmodulemd

* Tue May 26 2020 Evgeni Golov - 3.3.1-2
- remove "solv" dependency from setup.py as python3-solv does not provide an egg

* Fri May 08 2020 Evgeni Golov - 3.3.1-1
- Release python-pulp-rpm 3.3.1

* Thu Apr 30 2020 Evgeni Golov - 3.3.0-1
- Initial package.
