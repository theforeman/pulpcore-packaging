%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name setuptools-rust

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 41
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel


%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-semantic-version >= 2.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.7.4

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
%doc README.md
%{python3_sitelib}/setuptools_rust
%{python3_sitelib}/setuptools_rust-*-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.6.0-1
- Release python-setuptools-rust 1.6.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.11.5-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane - 0.11.5-2
- Build against python 3.9.

* Thu Sep 09 2021 Evgeni Golov - 0.11.5-1
- Initial package.
