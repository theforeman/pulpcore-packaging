# Created by pyp2rpm-3.3.3
%global pypi_name pulp-deb

Name:           python-%{pypi_name}
Version:        2.6.1
Release:        1%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-debian >= 0.1.36
BuildRequires:  python3-pulpcore < 3.7
BuildRequires:  python3-pulpcore >= 3.6
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-debian >= 0.1.36
Requires:       python3-pulpcore < 3.7
Requires:       python3-pulpcore >= 3.6
Requires:       python3-setuptools

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
%license LICENSE
%doc README.md
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 03 2020 Evgeni Golov 2.6.1-1
- Update to 2.6.1

* Thu Jun 18 2020 Evgeni Golov - 2.4.0-0.1.b1
- Update to 2.4.0b1

* Thu Apr 30 2020 ATIX AG <info@atix.de> - 2.3.0-0.1.b1
- Initial package.
