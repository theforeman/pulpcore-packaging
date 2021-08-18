# Created by pyp2rpm-3.3.6
%global pypi_name pulp-cli

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        1%{?dist}
Summary:        Command line interface to talk to pulpcore's REST API

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-PyYAML < 6.0
Requires:       python%{python3_pkgversion}-PyYAML >= 5.3
Requires:       python%{python3_pkgversion}-click < 9
Requires:       python%{python3_pkgversion}-click >= 7.1.2
Requires:       python%{python3_pkgversion}-click-shell < 3
Requires:       python%{python3_pkgversion}-click-shell >= 2.1
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pygments
Requires:       python%{python3_pkgversion}-requests < 3.0
Requires:       python%{python3_pkgversion}-requests >= 2.24
Requires:       python%{python3_pkgversion}-schema = 0.7.4
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-toml = 0.10.2
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
%{_bindir}/pulp
%{python3_sitelib}/pulp_cli
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pytest_pulp_cli
%{python3_sitelib}/pulp_cli-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 11 2021 Evgeni Golov - 0.11.0-1
- Release python-pulp-cli 0.11.0

* Wed Jun 30 2021 Evgeni Golov - 0.10.1-1
- Initial package.

