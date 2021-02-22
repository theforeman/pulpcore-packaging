# Created by pyp2rpm-3.3.3
%global pypi_name bleach-allowlist

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Curated lists of tags and attributes for sanitizing html

License:        BSD License
URL:            https://github.com/yourcelf/bleach-allowlist.git
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.rst
%{python3_sitelib}/bleach_allowlist
%{python3_sitelib}/bleach_allowlist-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Feb 22 2021 Evgeni Golov - 1.0.3-1
- Release python-bleach-allowlist 1.0.3

* Mon Aug 10 2020 Evgeni Golov 0.0.11-1
- Update to 0.0.11

* Tue Jun 23 2020 Evgeni Golov - 0.0.10-1
- Initial package.
