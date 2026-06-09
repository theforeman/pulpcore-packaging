%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-python
%global src_name pulp_python

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.27.4
Release:        1%{?dist}
Summary:        pulp-python plugin for the Pulp Project

License:        GPLv2+
URL:            https://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-bandersnatch >= 6.6.0
Requires:       python%{python3_pkgversion}-bandersnatch < 6.7
Requires:       python%{python3_pkgversion}-pkginfo >= 1.12.0
Requires:       python%{python3_pkgversion}-pkginfo < 1.13.0
Requires:       python%{python3_pkgversion}-pulpcore >= 3.85.3
Requires:       python%{python3_pkgversion}-pulpcore < 3.115
Requires:       python%{python3_pkgversion}-pypi-simple >= 1.8.0
Requires:       python%{python3_pkgversion}-pypi-simple < 2.0
Requires:       python%{python3_pkgversion}-pypi-attestations == 0.0.28

Provides:       pulpcore-plugin(python) = %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%{python3_sitelib}/pulp_python
%{python3_sitelib}/pulp_python-%{version}.dist-info/


%changelog
* Tue Jun 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.4-1
- Update to 3.27.4

* Wed May 27 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.3-1
- Update to 3.27.3

* Fri Apr 17 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.2-1
- Update to 3.27.2

* Tue Apr 14 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.0-1
- Update to 3.27.0
- Sync bandersnatch bounds: >= 6.6.0, < 6.7
- Sync pypi-simple lower bound: >= 1.8.0
- Sync pulpcore bounds: >= 3.85.3, < 3.115
- Add pypi-attestations == 0.0.28 (new upstream dep)

* Tue Oct 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.19.1-1
- Update to 3.19.1

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.19.0-1
- Update to 3.19.0

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.13.5-1
- Update to 3.13.5

* Fri Apr 11 2025 Odilon Sousa <osousa@redhat.com> - 3.13.4-2
- Update requirements for bandersnatch

* Fri Apr 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.13.4-1
- Update to 3.13.4

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 3.13.2-3
- Add obsoletes for python3.11 package

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 3.13.2-2
- Add provides pulpcore-plugin(python)

* Mon Mar 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.13.2-1
- Update to 3.13.2

* Wed Feb 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.12.6-1
- Update to 3.12.6

* Mon Oct 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.12.5-1
- Update to 3.12.5

* Tue Oct 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.12.3-1
- Update to 3.12.3

* Thu Sep 19 2024 Odilon Sousa <osousa@redhat.com> - 3.11.3-2
- Remove packaging requirement

* Mon Sep 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.11.3-1
- Update to 3.11.3

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 3.11.2-1
- Release python-pulp-python 3.11.2

* Fri Apr 19 2024 Odilon Sousa <osousa@redhat.com> - 3.11.1-1
- Release python-pulp-python 3.11.1

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.11.0-1
- Release python-pulp-python 3.11.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.10.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-3
- Obsolete python39 packages for a smooth upgrade

* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-2
- Rebuild against python 3.11

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-1
- Release python-pulp-python 3.10.0

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.8.0-1
- Release python-pulp-python 3.8.0

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 3.7.2-2
- Fixing operator logic on Conflicts for pulpcore

* Tue Sep 20 2022 Odilon Sousa 3.7.2-1
- Update to 3.7.2

* Thu Jun 30 2022 Ian Ballou <ianballou67@gmail.com> - 3.7.1-1
- Release pulp-python 3.7.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.6.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.6.0-4
- Build against python 3.9

* Wed Feb 23 2022 Odilon Sousa <osousa@redhat.com> - 3.6.0-3
- Adding pypi-simple as dependency

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 3.6.0-2
- Fixup dependency issues

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.6.0-1
- Release python-pulp-python 3.6.0

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 3.5.2-1
- Release python-pulp-python 3.5.2

* Mon Oct 18 2021 Evgeni Golov - 3.5.1-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 3.5.1-1
- Update to 3.5.1

* Wed Sep 08 2021 Evgeni Golov 3.5.0-1
- Update to 3.5.0

* Tue Jul 13 2021 Evgeni Golov - 3.4.0-1
- Initial package.
