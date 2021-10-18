# Created by pyp2rpm-3.3.3
%global pypi_name pulp-python

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        2%{?dist}
Summary:        pulp-python plugin for the Pulp Project

License:        GPLv2+
URL:            https://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-bandersnatch = 4.4.0
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pkginfo
Requires:       python%{python3_pkgversion}-pulpcore < 3.15
Requires:       python%{python3_pkgversion}-pulpcore >= 3.13
Requires:       python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(python) = %{version}

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
%{python3_sitelib}/pulp_python
%{python3_sitelib}/pulp_python-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 19 2021 Evgeni Golov - 3.4.0-2
- Add provides for 'pulpcore-plugin'

* Tue Jul 13 2021 Evgeni Golov - 3.4.0-1
- Initial package.
