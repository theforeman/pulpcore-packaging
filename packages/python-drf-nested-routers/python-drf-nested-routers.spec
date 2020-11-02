# Created by pyp2rpm-3.3.3
%global pypi_name drf-nested-routers

Name:           python-%{pypi_name}
Version:        0.92.1
Release:        1%{?dist}
Summary:        Nested resources for the Django Rest Framework

License:        Apache
URL:            https://github.com/alanjds/drf-nested-routers
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 1.11
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.6.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md README.rst
%{python3_sitelib}/rest_framework_nested
%{python3_sitelib}/rest_framework_nested/runtests
%{python3_sitelib}/drf_nested_routers-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 02 2020 Evgeni Golov 0.92.1-1
- Update to 0.92.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.91-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.91-1
- Initial package.
