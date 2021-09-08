%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name drf-yasg

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.17.1
Release:        2%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code

License:        BSD License
URL:            https://github.com/axnsan12/drf-yasg
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coreapi >= 2.3.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coreschema >= 0.0.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-inflection >= 0.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 1.11.7	
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-rest-framework >= 3.8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ruamel-yaml >= 0.15.34
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uritemplate >= 3.0.0


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
%license docs/license.rst LICENSE.rst
%doc docs/readme.rst README.rst
%{python3_sitelib}/drf_yasg
%{python3_sitelib}/drf_yasg-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 1.17.1-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 1.17.1-1
- Update to 1.17.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.17.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.17.0-1
- Initial package.
