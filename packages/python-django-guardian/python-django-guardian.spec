# Created by pyp2rpm-3.3.3
%global pypi_name django-guardian

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        1%{?dist}
Summary:        Implementation of per object permissions for Django

License:        BSD
URL:            http://github.com/django-guardian/django-guardian
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django >= 2.2
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.2

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/guardian
%{python3_sitelib}/django_guardian-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 25 2020 Evgeni Golov - 2.3.0-1
- Initial package.
