%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name setuptools-rust

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.11.5
Release:        1%{?dist}
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-semantic-version >= 2.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 41
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-toml >= 0.9
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel


%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-semantic-version >= 2.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-toml >= 0.9

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
%license LICENSE
%doc README.md examples/html-py-ever/README.md examples/tomlgen/README.rst
%{python3_sitelib}/setuptools_rust
%{python3_sitelib}/setuptools_rust-*-py%{python3_version}.egg-info


%changelog
* Thu Sep 09 2021 Evgeni Golov - 0.11.5-1
- Initial package.
