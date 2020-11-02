# Created by pyp2rpm-3.3.3
%global pypi_name django-import-export

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        1%{?dist}
Summary:        Django application and library for importing and exporting data with included admin integration

License:        BSD License
URL:            https://github.com/django-import-export/django-import-export
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.0
Requires:       python%{python3_pkgversion}-diff-match-patch
Requires:       python%{python3_pkgversion}-tablib >= 0.14.0

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
%doc README.rst
%{python3_sitelib}/import_export
%{python3_sitelib}/django_import_export-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 02 2020 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Tue Aug 25 2020 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Tue Apr 28 2020 Evgeni Golov - 2.0.2-1
- Initial package.
