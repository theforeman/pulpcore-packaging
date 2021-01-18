# Created by pyp2rpm-3.3.5
%global pypi_name django-guid

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Middleware that makes a request GUID available from anywhere and injects it into your logs

License:        BSD
URL:            https://github.com/JonasKs/django-guid
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         django-guid-setup-py.patch
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
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitelib}/demoproj
%{python3_sitelib}/django_guid
%{python3_sitelib}/tests
%{python3_sitelib}/django_guid-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 18 2021 Evgeni Golov - 2.2.0-1
- Initial package.
