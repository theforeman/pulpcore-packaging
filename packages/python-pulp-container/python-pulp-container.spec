%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-container
%global src_name pulp_container

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.26.2
Release:        1%{?dist}
Summary:        Container plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-pulpcore < 3.100
Requires:       python%{python3_pkgversion}-pulpcore >= 3.75
Requires:       python%{python3_pkgversion}-pyjwt >= 2.4
Conflicts:      python%{python3_pkgversion}-pyjwt >= 2.11
Requires:       python%{python3_pkgversion}-jsonschema >= 4.4
Requires:       python%{python3_pkgversion}-jsonschema < 4.24

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Provides:       pulpcore-plugin(container) = %{version}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Tue Oct 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.26.2-1
- Update to 2.26.2

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.26.1-1
- Update to 2.26.1

* Wed Apr 30 2025 Odilon Sousa <osousa@redhat.com> - 2.24.2-2
- Update requirement for pyjwt

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.2-1
- Update to 2.24.2

* Fri Apr 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.1-1
- Update to 2.24.1

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.24.0-3
- Add obsoletes for python3.11 package

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.24.0-2
- Add provides pulpcore-plugin(contaier)

* Mon Mar 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.0-1
- Update to 2.24.0

* Thu Jan 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.22.1-1
- Update to 2.22.1

* Mon Nov 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.22.0-1
- Update to 2.22.0

* Mon Oct 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.21.1-1
- Update to 2.21.1

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.21.0-1
- Update to 2.21.0

* Tue Sep 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.20.3-1
- Update to 2.20.3

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 2.20.2-1
- Release python-pulp-container 2.20.2

* Thu Jul 25 2024 Odilon Sousa <osousa@redhat.com> - 2.20.1-1
- Release python-pulp-container 2.20.1

* Mon May 06 2024 Odilon Sousa <osousa@redhat.com> - 2.20.0-1
- Release python-pulp-container 2.20.0

* Wed Apr 24 2024 Odilon Sousa <osousa@redhat.com> - 2.19.3-1
- Release python-pulp-container 2.19.3

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 2.19.2-1
- Release python-pulp-container 2.19.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.16.3-2
- Remove SCL bits

* Thu Jan 04 2024 Odilon Sousa <osousa@redhat.com> - 2.16.3-1
- Release python-pulp-container 2.16.3

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 2.16.2-2
- Obsolete python39 packages for a smooth upgrade

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 2.16.2-1
- Release python-pulp-container 2.16.2

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 2.15.2-1
- Release python-pulp-container 2.15.2

* Thu Apr 27 2023 Evgeni Golov - 2.14.5-1
- Release python-pulp-container 2.14.5

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 2.14.3-2
- Bump python-ecdsa requirement

* Wed Jan 04 2023 Odilon Sousa <osousa@redhat.com> - 2.14.3-1
- Release python-pulp-container 2.14.3

* Tue Nov 01 2022 Ian Ballou <ianballou67@gmail.com> - 2.14.2-1
- Update to 2.14.2

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.14.0-2
- Fixing Loosen requirements for jsonschema

* Tue Sep 20 2022 Odilon Sousa 2.14.0-1
- Update to 2.14.0

* Mon Aug 22 2022 Odilon Sousa <osousa@redhat.com> - 2.10.7-1
- Release python-pulp-container 2.10.7

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri May 06 2022 Odilon Sousa <osousa@redhat.com> - 2.10.3-3
- Rebuilding with python_disable_dependency_generator macro

* Mon May 02 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-2
- Build against python 3.9

* Mon May 02 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-1
- Release python-pulp-container 2.10.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.0-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 2.10.0-1
- Release python-pulp-container 2.10.0

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 2.9.0-1
- Release python-pulp-container 2.9.0

* Mon Oct 18 2021 Evgeni Golov - 2.8.1-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 2.8.1-1
- Update to 2.8.1

* Wed Sep 08 2021 Evgeni Golov 2.8.0-1
- Update to 2.8.0

* Wed Jul 28 2021 Odilon Sousa <osousa@redhat.com> - 2.7.1-1
- Release python-pulp-container 2.7.1

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
