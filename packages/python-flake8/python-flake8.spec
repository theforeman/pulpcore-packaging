# Created by pyp2rpm-3.3.3
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        3.9.0
Release:        1%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co

License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-mccabe < 0.7.0
Requires:       python%{python3_pkgversion}-mccabe >= 0.6.0
Requires:       python%{python3_pkgversion}-pycodestyle < 2.8.0
Requires:       python%{python3_pkgversion}-pycodestyle >= 2.7.0
Requires:       python%{python3_pkgversion}-pyflakes < 2.4.0
Requires:       python%{python3_pkgversion}-pyflakes >= 2.3.0
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst tests/fixtures/config_files/README.rst
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 3.9.0-1
- Update to 3.9.0

* Thu Oct 29 2020 Evgeni Golov 3.8.4-1
- Update to 3.8.4

* Tue Jun 23 2020 Evgeni Golov - 3.8.3-1
- Initial package.
