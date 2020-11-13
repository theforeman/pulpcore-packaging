# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-importer

Name:           python-%{pypi_name}
Version:        0.2.11
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
Requires:       ansible-lint < 5.0
Requires:       ansible-lint >= 4.2.0
%endif
Requires:       python%{python3_pkgversion}-ansible-builder >= 0.2.1
Requires:       python%{python3_pkgversion}-ansible-builder < 1.0
Requires:       python%{python3_pkgversion}-attrs < 21
Requires:       python%{python3_pkgversion}-attrs >= 19.3.0
Requires:       python%{python3_pkgversion}-bleach < 4
Requires:       python%{python3_pkgversion}-bleach >= 3.1.3
Requires:       python%{python3_pkgversion}-bleach-whitelist < 1
Requires:       python%{python3_pkgversion}-bleach-whitelist >= 0.0.10
Requires:       python%{python3_pkgversion}-flake8 < 4
Requires:       python%{python3_pkgversion}-flake8 >= 3.7.9
Requires:       python%{python3_pkgversion}-markdown < 4
Requires:       python%{python3_pkgversion}-markdown >= 3.2.1
Requires:       python%{python3_pkgversion}-pyyaml < 6
Requires:       python%{python3_pkgversion}-pyyaml >= 5.2
Requires:       python%{python3_pkgversion}-requests < 3
Requires:       python%{python3_pkgversion}-requests >= 2.23.0
Requires:       python%{python3_pkgversion}-semantic-version < 3
Requires:       python%{python3_pkgversion}-semantic-version >= 2.8.4

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n galaxy_importer-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i -E '/\s+ansible($|-lint)/d' setup.cfg

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license galaxy_importer/utils/spdx_licenses.py galaxy_importer/utils/spdx_licenses.json
%doc README.md
%{python3_sitelib}/galaxy_importer
%{python3_sitelib}/galaxy_importer-%{version}-py%{python3_version}.egg-info

%changelog
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
