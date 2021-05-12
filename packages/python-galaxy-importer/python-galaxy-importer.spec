# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-importer

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Galaxy content importer

License:        Apache-2.0
URL:            https://github.com/ansible/galaxy-importer
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/galaxy_importer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# We don't care if Ansible is Python 2 or 3 as we just call the CLI
Requires:       ansible
Requires:       /usr/bin/ansible-test
%if 0%{?rhel} == 8
# We only have ansible-lint built on EL8
Requires:       ansible-lint < 6.0
Requires:       ansible-lint >= 5.0.8
%endif
Requires:       python%{python3_pkgversion}-attrs < 22
Requires:       python%{python3_pkgversion}-attrs >= 21.2.0
Requires:       python%{python3_pkgversion}-bleach < 4
Requires:       python%{python3_pkgversion}-bleach >= 3.3.0
Requires:       python%{python3_pkgversion}-bleach-allowlist < 2
Requires:       python%{python3_pkgversion}-bleach-allowlist >= 1.0.3
Requires:       python%{python3_pkgversion}-flake8 < 4
Requires:       python%{python3_pkgversion}-flake8 >= 3.9.2
Requires:       python%{python3_pkgversion}-markdown < 4
Requires:       python%{python3_pkgversion}-markdown >= 3.3.4
Requires:       python%{python3_pkgversion}-pyyaml < 6
Requires:       python%{python3_pkgversion}-pyyaml >= 5.4.1
Requires:       python%{python3_pkgversion}-requests < 3
Requires:       python%{python3_pkgversion}-requests >= 2.25.1
Requires:       python%{python3_pkgversion}-semantic-version < 3
Requires:       python%{python3_pkgversion}-semantic-version >= 2.8.5
Requires:       tar

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n galaxy_importer-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i -E '/\s+ansible($|-core|-lint)/d' setup.cfg

%build
%py3_build

%install
%py3_install
install -d -m 0755 %{buildroot}/%{_sysconfdir}/galaxy-importer/

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/galaxy_importer
%{python3_sitelib}/galaxy_importer-%{version}-py%{python3_version}.egg-info
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/galaxy-importer

%changelog
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
