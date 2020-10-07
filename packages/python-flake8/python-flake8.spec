# Created by pyp2rpm-3.3.3
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        3.8.4
Release:        1%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co

License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-configparser
BuildRequires:  python3-enum34
BuildRequires:  python3-functools32
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-mccabe < 0.7.0
BuildRequires:  python3-mccabe >= 0.6.0
BuildRequires:  python3-pycodestyle < 2.7.0
BuildRequires:  python3-pycodestyle >= 2.6.0a1
BuildRequires:  python3-pyflakes < 2.3.0
BuildRequires:  python3-pyflakes >= 2.2.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-typing

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-configparser
Requires:       python3-enum34
Requires:       python3-functools32
Requires:       python3-importlib-metadata
Requires:       python3-mccabe < 0.7.0
Requires:       python3-mccabe >= 0.6.0
Requires:       python3-pycodestyle < 2.7.0
Requires:       python3-pycodestyle >= 2.6.0a1
Requires:       python3-pyflakes < 2.3.0
Requires:       python3-pyflakes >= 2.2.0
Requires:       python3-setuptools
Requires:       python3-typing

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
%doc README.rst tests/fixtures/config_files/README.rst
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 3.8.4-1
- Update to 3.8.4

* Tue Jun 23 2020 Evgeni Golov - 3.8.3-1
- Initial package.
