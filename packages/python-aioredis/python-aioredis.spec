# Created by pyp2rpm-3.3.6
%global pypi_name aioredis
%global real_version %{version}b1

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        0.1.b1%{?dist}
Summary:        asyncio (PEP 3156) Redis support

License:        MIT
URL:            https://github.com/aio-libs/aioredis
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{real_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-async-timeout
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-typing-extensions

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-async-timeout
Requires:       python%{python3_pkgversion}-typing-extensions

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{real_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{real_version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov 2.0.0-0.1.b1
- Update to 2.0.0b1

* Fri Jul 02 2021 Evgeni Golov - 2.0.0-0.1.a1
- Initial package.
