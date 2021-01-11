# Created by pyp2rpm-3.3.3
%global pypi_name async-lru

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Simple lru_cache for asyncio

License:        None
URL:            https://github.com/wikibusiness/async_lru
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/async_lru-%{version}.tar.gz
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
%autosetup -n async_lru-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/async_lru.*
%{python3_sitelib}/async_lru.py
%{python3_sitelib}/async_lru-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 11 2021 Evgeni Golov - 1.0.2-1
- Initial package.
