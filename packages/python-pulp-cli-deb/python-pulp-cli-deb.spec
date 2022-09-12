%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name pulp-cli-deb

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.0.2
Release:        2%{?dist}
Summary:        Command line interface (CLI) for Pulp's pulp_deb plugin.

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli-deb
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-cli
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

Provides:       %{pypi_name} = %{version}

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_cli_deb-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 12 2022 Markus Bucher <bucher@atix.de> - 0.0.2-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Mon Dec 27 2021 Quirin Pamp <pamp@atix.de> - 0.0.2-1
- Release version 0.0.2.

* Fri Nov 05 2021 Maarten Beeckmans <maartenb@inuits.eu> - 0.0.1-1
- Initial package.
