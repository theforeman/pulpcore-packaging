# Created by pyp2rpm-3.3.3
%global pypi_name asyncio-throttle

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Simple, easy-to-use throttler for asyncio

License:        MIT
URL:            https://github.com/hallazzang/asyncio-throttle
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%license LICENSE
%doc README.md
%{python3_sitelib}/asyncio_throttle
%{python3_sitelib}/asyncio_throttle-%{version}-py%{python3_version}.egg-info

%changelog
* Wed May 12 2021 Evgeni Golov 1.0.2-1
- Update to 1.0.2

* Fri Mar 19 2021 Evgeni Golov - 1.0.1-1
- Initial package.
