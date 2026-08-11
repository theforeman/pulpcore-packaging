%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12


# Created by pyp2rpm-3.3.3
%global pypi_name pulp-ansible
%global src_name pulp_ansible

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.29.9
Release:        1%{?dist}
Epoch:          1
Summary:        Pulp plugin to manage Ansible content, e.g. roles

License:        GPLv2+
URL:            https://github.com/pulp/pulp_ansible
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-gitpython >= 3.1.24
Requires:       python%{python3_pkgversion}-gitpython < 3.2
Requires:       python%{python3_pkgversion}-PyYAML >= 6.0.2
Requires:       python%{python3_pkgversion}-PyYAML < 7.0
Requires:       python%{python3_pkgversion}-galaxy-importer >= 0.4.27
Requires:       python%{python3_pkgversion}-galaxy-importer < 0.5
Requires:       python%{python3_pkgversion}-jsonschema >= 4.9
Requires:       python%{python3_pkgversion}-jsonschema < 4.26
Requires:       python%{python3_pkgversion}-pulpcore >= 3.85
Requires:       python%{python3_pkgversion}-pulpcore < 3.115
Requires:       python%{python3_pkgversion}-semantic-version >= 2.9
Requires:       python%{python3_pkgversion}-semantic-version < 2.11
Requires:       python%{python3_pkgversion}-pillow >= 10.3
Requires:       python%{python3_pkgversion}-pillow < 13

Provides:       pulpcore-plugin(ansible) = %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{epoch}:%{version}-%{release}

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
* Tue Aug 11 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.29.9-1
- Update to 0.29.9

* Fri Jul 31 2026 Odilon Sousa <osousa@redhat.com> - 1:0.29.8-2
- Bump release for EL10 rebuild

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.29.8-1
- Update to 0.29.8

* Fri Apr 17 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.29.7-1
- Update to 0.29.7
- Replace Conflicts with Requires upper bounds: gitpython < 3.2, galaxy-importer < 0.5, semantic-version < 2.11

* Tue Apr 14 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.29.5-1
- Update to 0.29.5
- Remove async-lru dep (dropped upstream since 0.28.x)
- Sync galaxy-importer lower bound: >= 0.4.27
- Sync pulpcore upper bound: < 3.115

* Wed Mar 25 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.28.6-1
- Update to 0.28.6

* Tue Mar 17 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.28.5-1
- Update to 0.28.5

* Mon Jan 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.28.1-1
- Update to 0.28.1

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.28.0-1
- Update to 0.28.0

* Wed Jul 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.24.7-1
- Update to 0.24.7

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.24.6-1
- Update to 0.24.6

* Fri Apr 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.24.4-1
- Update to 0.24.4

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 1:0.24.3-3
- Add epoch to obsoletes

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 1:0.24.3-2
- Add obsoletes for python3.11 package

* Fri Apr 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.24.3-1
- Update to 0.24.3

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 1:0.24.1-3
- Add provides pulpcore-plugin(ansible)

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 1:0.24.1-2
- Update pulpcore requirement

* Mon Mar 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.24.1-1
- Update to 0.24.1

* Fri Mar 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.22.4-1
- Update to 0.22.4

* Thu Nov 14 2024 Odilon Sousa <osousa@redhat.com> - 1:0.22.3-2
- Update python-pulp-ansible with macro to disable dependency generation

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.22.3-1
- Update to 0.22.3

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.22.2-1
- Update to 0.22.2

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.22.1-1
- Update to 0.22.1

* Mon Sep 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.21.8-1
- Update to 0.21.8

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 1:0.21.7-1
- Release python-pulp-ansible 0.21.7

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 1:0.21.6-1
- Release python-pulp-ansible 0.21.6

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 1:0.21.5-1
- Release python-pulp-ansible 0.21.5

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 1:0.21.3-1
- Release python-pulp-ansible 0.21.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1:0.20.2-4
- Remove SCL bits

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 1:0.20.2-3
- Add epoch to overrides

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1:0.20.2-2
- Obsolete python39 packages for a smooth upgrade

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 1:0.20.2-1
- Release python-pulp-ansible 0.20.2

* Thu Sep 21 2023 Ian Ballou <ianballou67@gmail.com> - 1:0.18.1-1
- Update to 0.18.1

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 1:0.18.0-2
- Add python-pillow as dependency

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 1:0.18.0-1
- Release python-pulp-ansible 0.18.0

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 1:0.16.0-1
- Release python-pulp-ansible 0.16.0

* Wed Sep 28 2022 Odilon Sousa <osousa@redhat.com> - 1:0.15.0-1
- Release python-pulp-ansible 0.15.0

* Tue Sep 20 2022 Odilon Sousa 1:0.14.2-1
- Update to 0.14.2

* Tue Aug 30 2022 Odilon Sousa <osousa@redhat.com> - 1:0.13.2-2
- Fixing requirements for pulp-ansible with aiofiles

* Tue Aug 23 2022 Odilon Sousa <osousa@redhat.com> - 1:0.13.2-1
- Release python-pulp-ansible 0.13.2

* Fri May 13 2022 Yanis Guenane <yguenane@redhat.com> - 1:0.13.0-3
- Obsolete the old Python 3.8 package with epoch

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 1:0.13.0-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Mon May 02 2022 Yanis Guenane <yguenane@redhat.com> - 1:0.13.0-1
- Release python-pulp-ansible 0.13.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1:0.12.0-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 1:0.12.0-1
- Release python-pulp-ansible 0.12.0

* Wed Oct 20 2021 Odilon Sousa <osousa@redhat.com> - 1:0.10.1-1
- Release python-pulp-ansible 0.10.1

* Mon Oct 18 2021 Evgeni Golov - 1:0.10.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name
- Fix Epoch that was forgotten in 0.10.0-1

* Wed Sep 08 2021 Evgeni Golov 0.10.0-1
- Update to 0.10.0

* Thu Jul 29 2021 Odilon Sousa <osousa@redhat.com> - 1:0.9.0-1
- Release python-pulp-ansible 0.9.0

* Wed Jul 28 2021 Odilon Sousa <osousa@redhat.com> - 1:0.8.1-1
- Release python-pulp-ansible 0.8.1

* Fri Jun 11 2021 Evgeni Golov 1:0.8.0-1
- Update to 0.8.0

* Wed May 12 2021 Evgeni Golov 1:0.7.3-1
- Update to 0.7.3

* Fri Mar 19 2021 Evgeni Golov 1:0.7.1-1
- Update to 0.7.1

* Mon Jan 11 2021 Evgeni Golov 1:0.6.0-1
- Update to 0.6.0

* Fri Dec 18 2020 Evgeni Golov - 1:0.5.5-1
- Release python-pulp-ansible 0.5.5

* Wed Dec 09 2020 Evgeni Golov - 1:0.5.4-1
- Release python-pulp-ansible 0.5.4

* Wed Dec 09 2020 Evgeni Golov - 1:0.5.3-1
- Release python-pulp-ansible 0.5.3

* Thu Nov 26 2020 Evgeni Golov - 1:0.5.2-1
- Release python-pulp-ansible 0.5.2

* Tue Nov 10 2020 Evgeni Golov - 1:0.5.1-1
- Release python-pulp-ansible 0.5.1

* Tue Nov 03 2020 Evgeni Golov 1:0.5.0-1
- Update to 0.5.0

* Fri Oct 23 2020 Evgeni Golov - 1:0.4.2-1
- Release python-pulp-ansible 0.4.2

* Thu Oct 01 2020 Evgeni Golov - 1:0.4.1-1
- Release python-pulp-ansible 0.4.1

* Mon Sep 28 2020 Evgeni Golov 1:0.4.0-1
- Update to 0.4.0

* Thu Sep 10 2020 Evgeni Golov 1:0.3.0-1
- Update to 0.3.0

* Tue Aug 25 2020 Evgeni Golov 1:0.2.0-1
- Update to 0.2.0

* Mon Aug 10 2020 Evgeni Golov 0.2.0b15-1
- Update to 0.2.0b15

* Mon Jul 27 2020 Evgeni Golov - 0.2.0b14-2
* Fix pyyaml dependency

* Tue Jun 23 2020 Evgeni Golov - 0.2.0b14-1
- Initial package.
