%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-importer

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.39
Release:        2%{?dist}
Summary:        Galaxy content importer

License:        Apache-2.0
URL:            https://github.com/ansible/galaxy-importer
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/galaxy_importer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

# We don't care if Ansible is Python 2 or 3 as we just call the CLI
Requires:       /usr/bin/ansible
Requires:       /usr/bin/ansible-test
Requires:       ansible-lint <= 26.4.0
Requires:       ansible-lint >= 6.2.2
Requires:       python%{python3_pkgversion}-ansible-builder < 4.0
Requires:       python%{python3_pkgversion}-ansible-builder >= 1.2.0
Requires:       python%{python3_pkgversion}-attrs < 23
Requires:       python%{python3_pkgversion}-attrs >= 21.4.0
Requires:       python%{python3_pkgversion}-flake8 < 7
Requires:       python%{python3_pkgversion}-flake8 >= 5.0.0
Requires:       python%{python3_pkgversion}-markdown < 4
Requires:       python%{python3_pkgversion}-markdown >= 3.3.4
Requires:       python%{python3_pkgversion}-nh3 < 3
Requires:       python%{python3_pkgversion}-nh3 >= 0.2.18
Requires:       python%{python3_pkgversion}-packaging < 27
Requires:       python%{python3_pkgversion}-packaging >= 23.2
Requires:       python%{python3_pkgversion}-pyyaml < 7
Requires:       python%{python3_pkgversion}-pyyaml >= 5.4.1
Requires:       python%{python3_pkgversion}-requests < 3
Requires:       python%{python3_pkgversion}-requests >= 2.28.0
Requires:       python%{python3_pkgversion}-semantic-version < 3
Requires:       python%{python3_pkgversion}-semantic-version >= 2.9.0
Requires:       tar

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n galaxy_importer-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i -E '/\s+ansible($|-core|-lint)/d' setup.cfg


%build
set -ex
%py3_build


%install
set -ex
%py3_install
install -d -m 0755 %{buildroot}/%{_sysconfdir}/galaxy-importer/


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/galaxy_importer
%{python3_sitelib}/galaxy_importer-%{version}-py%{python3_version}.egg-info
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/galaxy-importer


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.4.39-2
- Bump release for EL10 rebuild

* Fri May 29 2026 Odilon Sousa <osousa@redhat.com> - 0.4.39-1
- Update to 0.4.39
- Relax packaging bound: < 25 → < 27 (upstream: packaging<27,>=23.2)
- Add missing Requires: nh3 >= 0.2.18, < 3
- Update ansible-lint bounds: >= 6.2.2, <= 26.4.0 (upstream 0.4.39 requires ansible-lint>=6.2.2,<=26.4.0)
- Update ansible-builder lower bound: >= 1.2.0 (was >= 1.0.1)
- Drop bleach and bleach-allowlist Requires (removed upstream)

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.33-1
- Update to 0.4.33

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.4.19-5
- Add obsoletes for python3.11 package

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com>  - 0.4.19-4
- Rebuild against python3.12

* Mon Nov 25 2024 Evgeni Golov - 0.4.19-3
- make galaxy-importer require ansible-lint on EL9

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 0.4.19-2
- Update ansible-builder requirements

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 0.4.19-1
- Release python-galaxy-importer 0.4.19

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.4.7-2
- Remove SCL bits

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 0.4.7-1
- Release python-galaxy-importer 0.4.7

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.4.6-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.6-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 0.4.6-1
- Update to 0.4.6

* Tue Aug 23 2022 Odilon Sousa <osousa@redhat.com> - 0.4.5-1
- Release python-galaxy-importer 0.4.5

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-3
- Build against python 3.9

* Tue Feb 22 2022 Odilon Sousa <osousa@redhat.com> - 0.4.2-2
- Require /usr/bin/ansible

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 0.4.2-1
- Release python-galaxy-importer 0.4.2

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.4.1-1
- Release python-galaxy-importer 0.4.1

* Tue Oct 19 2021 Evgeni Golov - 0.4.0-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 0.4.0-1
- Update to 0.4.0

* Wed Sep 08 2021 Evgeni Golov - 0.3.2-3
- Correct non-SCL dependencies

* Mon Sep 06 2021 Evgeni Golov - 0.3.2-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 0.3.2-1
- Update to 0.3.2

* Wed Apr 14 2021 Yanis Guenane - 0.3.0-3
- Add tar as a runtime Requires
- Manage /etc/galaxy-importer folder

* Wed Mar 31 2021 Evgeni Golov - 0.3.0-2
- Fix ansible-lint requires

* Wed Mar 31 2021 Evgeni Golov 0.3.0-1
- Update to 0.3.0

* Mon Feb 22 2021 Evgeni Golov - 0.2.15-1
- Release python-galaxy-importer 0.2.15

* Wed Dec 09 2020 Evgeni Golov - 0.2.12-1
- Release python-galaxy-importer 0.2.12

* Fri Nov 13 2020 Evgeni Golov - 0.2.11-1
- Release python-galaxy-importer 0.2.11

* Thu Nov 05 2020 Evgeni Golov 0.2.9-1
- Update to 0.2.9

* Mon Aug 31 2020 Evgeni Golov 0.2.8-1
- Update to 0.2.8

* Mon Aug 10 2020 Evgeni Golov 0.2.8-0.1.rc9
- Update to 0.2.8rc9

* Mon Jul 27 2020 Evgeni Golov 0.2.7-1
- Update to 0.2.7

* Mon Jul 27 2020 Evgeni Golov - 0.2.5-2
- Patch out Ansible and ansible-lint dependencies from the Python egg

* Tue Jun 23 2020 Evgeni Golov - 0.2.5-1
- Initial package.
