# Created by pyp2rpm-3.3.3
%global pypi_name drf-access-policy

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Declarative access policies/permissions modeled after AWS' IAM policies

License:        MIT
URL:            https://github.com/rsinger86/drf-access-policy
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
%{python3_sitelib}/rest_access_policy
%{python3_sitelib}/drf_access_policy-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 28 2020 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Tue Aug 25 2020 Evgeni Golov - 0.6.2-1
- Initial package.
