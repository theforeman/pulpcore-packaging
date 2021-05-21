# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm-client

Name:           python-%{pypi_name}
Version:        3.11.0
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pulp_rpm-client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-certifi
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six >= 1.10
BuildRequires:  python%{python3_pkgversion}-urllib3 >= 1.15

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-certifi
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-six >= 1.10
Requires:       python%{python3_pkgversion}-urllib3 >= 1.15

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n pulp_rpm-client-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_rpm_client-%{version}-py%{python3_version}.egg-info

%changelog
* Fri May 21 2021 Evgeni Golov - 3.11.0-1
- Initial package.
