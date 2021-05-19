# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm

Name:           python-%{pypi_name}
Version:        3.11.0
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
Requires:       python36-gobject
Requires:       libmodulemd2
%else
Requires:       python3-gobject
Requires:       libmodulemd >= 2.0
%endif
Requires:       python%{python3_pkgversion}-createrepo_c >= 0.17.0
Conflicts:      python%{python3_pkgversion}-createrepo_c >= 0.18
Requires:       python%{python3_pkgversion}-django-readonly-field
Requires:       python%{python3_pkgversion}-jsonschema >= 3.0
Requires:       python%{python3_pkgversion}-libcomps >= 0.1.15
Conflicts:      python%{python3_pkgversion}-libcomps >= 0.2
Requires:       python%{python3_pkgversion}-productmd >= 1.25
Requires:       python%{python3_pkgversion}-pulpcore < 3.13
Requires:       python%{python3_pkgversion}-pulpcore >= 3.7
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-solv >= 0.7.17
Conflicts:      python%{python3_pkgversion}-solv >= 0.8

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove "solv" dependency from setup.py as python3-solv does not provide an egg
sed -i "/solv/d" requirements.txt

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_rpm
%{python3_sitelib}/pulp_rpm-%{version}-py%{python3_version}.egg-info

%changelog
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
