%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml
%global srcname ruamel-yaml

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.16.10
Release:        2%{?dist}
Summary:        ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

License:        MIT license
URL:            https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ruamel-yaml-clib


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT --install-purelib %{python3_sitelib} --install-platlib %{python3_sitearch} --install-scripts %{_bindir} --install-data %{_datadir}
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 0.16.10-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 0.16.10-1
- Update to 0.16.10

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.16.5-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.16.5-1
- Initial package.
