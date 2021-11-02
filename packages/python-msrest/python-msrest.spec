%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name msrest

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.6.21
Release:        1%{?dist}
Summary:        AutoRest swagger generator Python client runtime

License:        MIT License
URL:            https://github.com/Azure/msrest-for-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-certifi >= 2017.4.17
Requires:       %{?scl_prefix}python%{python3_pkgversion}-isodate >= 0.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.16
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests-oauthlib >= 0.5

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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 02 2021 Evgeni Golov - 0.6.21-1
- Initial package.
