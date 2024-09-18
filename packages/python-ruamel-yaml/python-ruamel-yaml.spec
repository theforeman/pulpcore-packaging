%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml
%global srcname ruamel-yaml

Name:           python-%{srcname}
Version:        0.18.6
Release:        1%{?dist}
Summary:        ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

License:        MIT license
URL:            https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  gcc
BuildRequires:  libyaml-devel

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-ruamel-yaml-clib >= 0.2.6


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT --install-purelib %{python3_sitelib} --install-platlib %{python3_sitearch} --install-scripts %{_bindir} --install-data %{_datadir}


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
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
