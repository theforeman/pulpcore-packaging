# Created by pyp2rpm-3.3.3
%global pypi_name urlman

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Django URL pattern helpers

License:        Apache-2.0
URL:            https://github.com/andrewgodwin/urlman
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%doc README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 1.4.0-1
- Update to 1.4.0

* Thu Nov 05 2020 Evgeni Golov - 1.3.0-2
- Fix License tag in spec file

* Tue Aug 25 2020 Evgeni Golov - 1.3.0-1
- Initial package.
