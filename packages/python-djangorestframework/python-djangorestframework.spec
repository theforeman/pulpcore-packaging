# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework

Name:           python-%{pypi_name}
Version:        3.12.1
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            https://www.django-rest-framework.org/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-django >= 2.2
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.2

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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/rest_framework
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 02 2020 Evgeni Golov 3.12.1-1
- Update to 3.12.1

* Thu Oct 29 2020 Evgeni Golov 3.11.2-1
- Update to 3.11.2

* Mon Sep 28 2020 Evgeni Golov 3.11.1-1
- Update to 3.11.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.10.3-1
- Initial package.
