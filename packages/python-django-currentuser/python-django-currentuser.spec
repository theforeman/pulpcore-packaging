# Created by pyp2rpm-3.3.3
%global pypi_name django-currentuser

Name:           python-%{pypi_name}
Version:        0.5.3
Release:        1%{?dist}
Summary:        Conveniently store reference to request user on thread/db level

License:        BSD
URL:            https://github.com/PaesslerAG/django-currentuser
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django < 3.3
Requires:       python%{python3_pkgversion}-django >= 1.11.17

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
%{python3_sitelib}/django_currentuser
%{python3_sitelib}/django_currentuser-%{version}-py%{python3_version}.egg-info

%changelog
* Wed May 12 2021 Evgeni Golov 0.5.3-1
- Update to 0.5.3

* Fri Mar 19 2021 Evgeni Golov 0.5.2-1
- Update to 0.5.2

* Tue Aug 25 2020 Evgeni Golov - 0.5.1-1
- Initial package.
