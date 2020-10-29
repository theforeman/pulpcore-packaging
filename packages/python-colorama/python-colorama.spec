# Created by pyp2rpm-3.3.3
%global pypi_name colorama

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        1%{?dist}
Summary:        Cross-platform colored terminal text

License:        BSD
URL:            https://github.com/tartley/colorama
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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

sed -i '/long_description=/ s/=.*/="colorama",/' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Oct 29 2020 Evgeni Golov 0.4.4-1
- Update to 0.4.4

* Tue Aug 25 2020 Evgeni Golov - 0.4.3-1
- Initial package.
