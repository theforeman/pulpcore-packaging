%global debug_package %{nil}
# Created by pyp2rpm-3.3.3
%global pypi_name PyYAML
%global srcname pyyaml

Name:           python-%{srcname}
Version:        5.4.1
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://pyyaml.org/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildRequires:  gcc
BuildRequires:  libyaml-devel

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python3-yaml}
Provides:       python3-yaml = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%{python3_sitearch}/_yaml
%{python3_sitearch}/yaml
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed May 12 2021 Evgeni Golov 5.4.1-1
- Update to 5.4.1

* Tue Jan  5 2021 Evgeni Golov - 5.3.1-3
- Also provide 'yaml' name

* Tue Aug 25 2020 Evgeni Golov - 5.3.1-2
- Provide PyYAML name too

* Tue Apr 14 2020 Evgeni Golov 5.3.1-1
- Update to 5.3.1

* Wed Mar 18 2020 Samir Jha 5.3-1
- Update to 5.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 5.2-1
- Update to 5.2

* Mon Nov 18 2019 Evgeni Golov - 5.1.2-1
- Initial package.
