# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml.clib
%global srcname ruamel-yaml-clib

Name:           python-%{srcname}
Version:        0.2.2
Release:        1%{?dist}
Summary:        C version of reader, parser and emitter for ruamel

License:        MIT
URL:            https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/ruamel
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 0.2.2-1
- Update to 0.2.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.2.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.2.0-1
- Initial package.
