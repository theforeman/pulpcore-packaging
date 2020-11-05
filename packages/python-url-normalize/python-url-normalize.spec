# Created by pyp2rpm-3.3.3
%global pypi_name url-normalize

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        2%{?dist}
Summary:        URL normalization for Python

License:        MIT
URL:            https://github.com/niksite/url-normalize
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-six

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/url_normalize
%{python3_sitelib}/url_normalize-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 05 2020 Evgeni Golov - 1.4.3-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 1.4.3-1
- Update to 1.4.3

* Tue Aug 25 2020 Evgeni Golov - 1.4.2-1
- Initial package.
