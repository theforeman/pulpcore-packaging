%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml
%global srcname ruamel-yaml
%global src_name ruamel_yaml

Name:           python%{python3_pkgversion}-%{srcname}
Version:        0.19.1
Release:        1%{?dist}
Summary:        ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

License:        MIT license
URL:            https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info


%changelog
* Thu Sep  3 21:39:56 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.19.1-1
- Update to 0.19.1
- Use a macro for the normalized source archive name

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.18.15-2
- Bump release for EL10 rebuild

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.15-1
- Update to 0.18.15
- Migrate to pyproject_wheel; remove gcc/libyaml-devel (pure Python)

* Sun Jun 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.14-1
- Update to 0.18.14

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 0.18.10-2
- Rebuild against python3.12

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.10-1
- Update to 0.18.10

* Mon Jan 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.9-1
- Update to 0.18.9

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.6-1
- Update to 0.18.6

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.17.21-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.17.21-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.17.21-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.17.21-3
- Build against python 3.11

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 0.17.21-2
- rebuilt

* Fri Feb 03 2023 Odilon Sousa 0.17.21-1
- Update to 0.17.21

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.17.20-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 0.17.20-1
- Release python-ruamel-yaml 0.17.20

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.17.17-1
- Release python-ruamel-yaml 0.17.17

* Mon Sep 06 2021 Evgeni Golov - 0.16.10-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 0.16.10-1
- Update to 0.16.10

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.16.5-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.16.5-1
- Initial package.
