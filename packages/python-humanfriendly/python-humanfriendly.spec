%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name humanfriendly

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        10.0
Release:        1%{?dist}
Summary:        Human friendly output for text interfaces using Python

License:        MIT
URL:            https://humanfriendly.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-capturer >= 2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coloredlogs >= 2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-monotonic
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyreadline
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyreadline3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-monotonic
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyreadline
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyreadline3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%license LICENSE.txt
%doc docs/readme.rst README.rst
%{_bindir}/humanfriendly
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Feb 07 2022 Odilon Sousa - 10.0-1
- Initial package.
