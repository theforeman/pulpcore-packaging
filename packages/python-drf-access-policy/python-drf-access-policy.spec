%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name drf-access-policy

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Declarative access policies/permissions modeled after AWS' IAM policies

License:        MIT
URL:            https://github.com/rsinger86/drf-access-policy
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyparsing


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
%doc README.md
%{python3_sitelib}/rest_access_policy
%{python3_sitelib}/drf_access_policy-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.1.0-2
- Build against python 3.9

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 1.1.0-1
- Release python-drf-access-policy 1.1.0

* Wed Sep 08 2021 Evgeni Golov 1.0.1-1
- Update to 1.0.1

* Mon Sep 06 2021 Evgeni Golov - 0.9.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 0.9.0-1
- Update to 0.9.0

* Fri Mar 19 2021 Evgeni Golov 0.8.7-1
- Update to 0.8.7

* Mon Nov 02 2020 Evgeni Golov 0.8.1-1
- Update to 0.8.1

* Mon Sep 28 2020 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Tue Aug 25 2020 Evgeni Golov - 0.6.2-1
- Initial package.
