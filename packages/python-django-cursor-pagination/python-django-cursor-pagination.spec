# Created by pyp2rpm-3.3.3
%global pypi_name django-cursor-pagination

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        1%{?dist}
Summary:        Cursor based pagination for Django

License:        BSD
URL:            https://github.com/photocrowd/django-cursor-pagination
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

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
%doc README.md
%{python3_sitelib}/__pycache__/cursor_pagination.*
%{python3_sitelib}/cursor_pagination.py
%{python3_sitelib}/django_cursor_pagination-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Aug 28 2020 Evgeni Golov - 0.1.4-1
- Initial package.
