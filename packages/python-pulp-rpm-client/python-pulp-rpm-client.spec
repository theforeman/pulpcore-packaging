%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.15.0
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pulp_rpm-client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-certifi
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-dateutil
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.15


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-certifi
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dateutil
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.15


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n pulp_rpm-client-%{version}
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
%doc README.md
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_rpm_client-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 08 2021 Evgeni Golov - 3.15.0-1
- Update to 3.15.0

* Thu Jul 08 2021 Evgeni Golov - 3.13.3-1
- Release python-pulp-rpm-client 3.13.3

* Tue Jun 29 2021 Evgeni Golov - 3.13.2-1
- Release python-pulp-rpm-client 3.13.2

* Thu Jun 17 2021 Evgeni Golov - 3.12.0-1
- Release python-pulp-rpm-client 3.12.0

* Fri May 21 2021 Evgeni Golov - 3.11.0-1
- Initial package.
