# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-ng

%global full_version %{version}b1

Name:           python-%{pypi_name}
Version:        4.2.0
Release:        0.1.b1%{?dist}
Summary:        galaxy-ng plugin for the Pulp Project

License:        GPLv2+
URL:            https://github.com/ansible/galaxy_ng/
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{full_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10
BuildRequires:  python3-wheel

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.2.3
Conflicts:      python3-django >= 2.3
Requires:       python3-certifi
Requires:       python3-dateutil
Requires:       python3-django-prometheus >= 2.0.0
Requires:       python3-drf-spectacular
Requires:       python3-pulp-ansible >= 1:0.3.0
Conflicts:      python3-pulp-ansible >= 1:0.4
Requires:       python3-pulpcore >= 3.6.0
Conflicts:      python3-pulpcore >= 3.7
Requires:       python3-setuptools
Requires:       python3-six >= 1.10
Requires:       python3-urllib3 >= 1.15

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{full_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/galaxy_ng
%{python3_sitelib}/galaxy_pulp
%{python3_sitelib}/galaxy_ng-%{full_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 14 2020 Evgeni Golov 4.2.0-0.1.b1
- Update to 4.2.0b1

* Fri Jul 17 2020 Evgeni Golov - 4.2.0-0.1.a10
- Initial package.
