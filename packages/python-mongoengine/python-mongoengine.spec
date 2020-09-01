# Created by pyp2rpm-3.3.3
%global pypi_name mongoengine

Name:           python-%{pypi_name}
Version:        0.20.0
Release:        1%{?dist}
Summary:        MongoEngine is a Python Object-Document Mapper for working with MongoDB

License:        MIT
URL:            http://mongoengine.org/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pymongo < 4.0
Requires:       python3-pymongo >= 3.4

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 01 2020 Evgeni Golov 0.20.0-1
- Update to 0.20.0

* Tue Mar 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.19.1-3
- Bump pymongo requires

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.19.1-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 0.19.1-1
- Initial package.
