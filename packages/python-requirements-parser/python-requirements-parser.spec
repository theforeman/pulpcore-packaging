# Created by pyp2rpm-3.3.3
%global pypi_name requirements-parser

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Parses Pip requirement files

License:        BSD
URL:            https://github.com/davidfischer/requirements-parser
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/requirements
%{python3_sitelib}/requirements_parser-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 05 2020 Evgeni Golov - 0.2.0-1
- Initial package.
