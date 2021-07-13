# Created by pyp2rpm-3.3.3
%global pypi_name importlib-resources

Name:           python-%{pypi_name}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Read resources from Python packages

License:        Apache2
URL:            https://github.com/python/importlib_resources
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_resources-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-zipp >= 0.4
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 3.4.1

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-zipp >= 0.4

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n importlib_resources-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/importlib_resources
%{python3_sitelib}/importlib_resources-*-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov - 5.0.0-1
- Initial package.
