%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name pulp-cli-deb
%global pypi_version 0.0.1

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Command line interface to talk to pulpcore's REST API

License:        GPLv2+
URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python3-devel
BuildRequires:  %{?scl_prefix}python3-setuptools


%description



%package -n     %{?scl_prefix}python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{?scl_prefix}python3-pulp-cli
Requires:       %{?scl_prefix}python3-click
Requires:       %{?scl_prefix}python3-setuptools

%description -n %{?scl_prefix}python3-%{pypi_name}




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{pypi_version}
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


%files -n %{?scl_prefix}python3-%{pypi_name}
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_cli_deb-%{pypi_version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 05 2021 Maarten Beeckmans <maartenb@inuits.eu> - 0.0.1-1
- Initial package.
