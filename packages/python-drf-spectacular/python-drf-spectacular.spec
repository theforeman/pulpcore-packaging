# Created by pyp2rpm-3.3.3
%global pypi_name drf-spectacular

Name:           python-%{pypi_name}
Version:        0.9.14
Release:        1%{?dist}
Summary:        Sane and flexible OpenAPI 3 schema generation for Django REST framework

License:        BSD
URL:            https://github.com/tfranzel/drf-spectacular
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-django >= 2.2
BuildRequires:  python%{python3_pkgversion}-pyyaml >= 5.1
BuildRequires:  python%{python3_pkgversion}-djangorestframework >= 3.10
BuildRequires:  python%{python3_pkgversion}-inflection >= 0.3.1
BuildRequires:  python%{python3_pkgversion}-jsonschema >= 2.6.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-uritemplate >= 2.0.0

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.2
Requires:       python%{python3_pkgversion}-pyyaml >= 5.1
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.10
Requires:       python%{python3_pkgversion}-inflection >= 0.3.1
Requires:       python%{python3_pkgversion}-jsonschema >= 2.6.0
Requires:       python%{python3_pkgversion}-uritemplate >= 2.0.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/long_description = readme.read.*/long_description = description/' setup.py

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE docs/license.rst
%doc README.rst docs/readme.rst
%{python3_sitelib}/drf_spectacular
%{python3_sitelib}/drf_spectacular/contrib
%{python3_sitelib}/drf_spectacular/management
%{python3_sitelib}/drf_spectacular/management/commands
%{python3_sitelib}/drf_spectacular/validation
%{python3_sitelib}/drf_spectacular-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 02 2020 Evgeni Golov 0.9.14-1
- Update to 0.9.14

* Mon Sep 28 2020 Evgeni Golov 0.9.13-1
- Update to 0.9.13

* Tue Aug 25 2020 Evgeni Golov - 0.9.12-1
- Initial package.
