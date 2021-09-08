%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name drf-spectacular

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.17.3
Release:        2%{?dist}
Summary:        Sane and flexible OpenAPI 3 schema generation for Django REST framework

License:        BSD
URL:            https://github.com/tfranzel/drf-spectacular
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.10
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-inflection >= 0.3.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jsonschema >= 2.6.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-uritemplate >= 2.0.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-inflection >= 0.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jsonschema >= 2.6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uritemplate >= 2.0.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/long_description = readme.read.*/long_description = description/' setup.py
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
%license LICENSE docs/license.rst
%doc README.rst docs/readme.rst
%{python3_sitelib}/drf_spectacular
%{python3_sitelib}/drf_spectacular/contrib
%{python3_sitelib}/drf_spectacular/management
%{python3_sitelib}/drf_spectacular/management/commands
%{python3_sitelib}/drf_spectacular/validation
%{python3_sitelib}/drf_spectacular-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 08 2021 Evgeni Golov - 0.17.3-2
- Build against Python 3.8

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 0.17.3-1
- Release python-drf-spectacular 0.17.3

* Fri Jul 02 2021 Evgeni Golov - 0.17.2-1
- Release python-drf-spectacular 0.17.2

* Fri Jun 11 2021 Evgeni Golov 0.16.0-1
- Update to 0.16.0

* Fri Mar 19 2021 Evgeni Golov 0.13.2-1
- Update to 0.13.2

* Mon Jan 11 2021 Evgeni Golov 0.11.0-1
- Update to 0.11.0

* Mon Nov 02 2020 Evgeni Golov 0.9.14-1
- Update to 0.9.14

* Mon Sep 28 2020 Evgeni Golov 0.9.13-1
- Update to 0.9.13

* Tue Aug 25 2020 Evgeni Golov - 0.9.12-1
- Initial package.
