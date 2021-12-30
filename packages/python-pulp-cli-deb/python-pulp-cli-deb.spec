%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name pulp-cli-deb

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Command line interface (CLI) for Pulp's pulp_deb plugin.

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli-deb
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{?scl_prefix}python3-pulp-cli
Requires:       %{?scl_prefix}python3-click
Requires:       %{?scl_prefix}python3-setuptools

%description -n %{?scl_prefix}python3-%{pypi_name}
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


%files -n %{?scl_prefix}python3-%{pypi_name}
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_cli_deb-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 05 2021 Maarten Beeckmans <maartenb@inuits.eu> - 0.0.1-1
- Initial package.
