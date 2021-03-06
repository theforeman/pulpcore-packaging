# Created by pyp2rpm-3.3.3
%global pypi_name python-dotenv
%global srcname dotenv

Name:           python-%{srcname}
Version:        0.14.0
Release:        2%{?dist}
Summary:        Add .env support to your django/flask apps in development and deployments

License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-click >= 5.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-typing

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-click >= 5.0
Requires:       python3-typing

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
%doc README.md
%{_bindir}/dotenv
%{python3_sitelib}/dotenv
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 05 2020 Evgeni Golov - 0.14.0-2
- Fix License tag in spec file

* Mon Jul 20 2020 Evgeni Golov 0.14.0-1
- Update to 0.14.0

* Tue Apr 28 2020 Evgeni Golov 0.13.0-1
- Update to 0.13.0

* Wed Mar 18 2020 Samir Jha 0.12.0-1
- Update to 0.12.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.10.3-1
- Initial package.
