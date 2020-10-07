# Created by pyp2rpm-3.3.3
%global pypi_name importlib-metadata

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Read metadata from Python packages

License:        Apache Software License
URL:            http://importlib-metadata.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-configparser >= 3.5
BuildRequires:  python3-contextlib2
BuildRequires:  python3-importlib-resources >= 1.3
BuildRequires:  python3-packaging
BuildRequires:  python3-pathlib2
BuildRequires:  python3-pep517
BuildRequires:  python3-rst-linker
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm
BuildRequires:  python3-zipp >= 0.5

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-configparser >= 3.5
Requires:       python3-contextlib2
Requires:       python3-importlib-resources >= 1.3
Requires:       python3-packaging
Requires:       python3-pathlib2
Requires:       python3-pep517
Requires:       python3-rst-linker
Requires:       python3-sphinx
Requires:       python3-zipp >= 0.5

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n importlib_metadata-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/importlib_metadata
%{python3_sitelib}/importlib_metadata-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 2.0.0-1
- Update to 2.0.0

* Mon Jul 20 2020 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Thu Jun 18 2020 Evgeni Golov 1.6.1-1
- Update to 1.6.1

* Thu Jun 04 2020 Evgeni Golov 1.6.0-1
- Update to 1.6.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 1.4.0-1
- Initial package.
