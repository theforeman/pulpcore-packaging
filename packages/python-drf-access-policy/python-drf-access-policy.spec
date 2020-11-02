# Created by pyp2rpm-3.3.3
%global pypi_name drf-access-policy

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Declarative access policies/permissions modeled after AWS' IAM policies

License:        MIT
URL:            https://github.com/rsinger86/drf-access-policy
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.md
%{python3_sitelib}/rest_access_policy
%{python3_sitelib}/drf_access_policy-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 02 2020 Evgeni Golov 0.8.1-1
- Update to 0.8.1

* Mon Sep 28 2020 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Tue Aug 25 2020 Evgeni Golov - 0.6.2-1
- Initial package.
