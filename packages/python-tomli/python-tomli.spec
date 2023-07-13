%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name tomli

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.0.1
Release:        1%{?dist}
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project2/tomli/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Upstream tomli uses flit, but we want to use setuptools on RHEL 8.
# This a downstream-only setup.py manually created from pyproject.toml metadata.
# It contains a @@VERSION@@ placeholder.
Source1:        001-tomli-setup.py

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
sed 's/@@VERSION@@/%{version}/' %{SOURCE1} > setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jul 13 2023 Odilon Sousa <osousa@redhat.com> - 2.0.1-1
- Initial package
