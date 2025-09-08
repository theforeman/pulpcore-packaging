%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-smart-proxy
%global src_name pulp_smart_proxy

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Smart Proxy plugin for the Pulp Project

License:        GPLv2+
URL:            https://theforeman.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-pulpcore < 3.85
Requires:       python%{python3_pkgversion}-pulpcore >= 3.49.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Provides:       pulpcore-plugin(smart_proxy) = %{version}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Mon Sep 08 2025 Evgeni Golov - 0.2.0-1
- Release python-pulp-smart-proxy 0.2.0

* Thu Jun 26 2025 Evgeni Golov - 0.1.0-1
- Release python-pulp-smart-proxy 0.1.0

* Tue Jun 17 2025 Evgeni Golov - 0.0.0-1
- Initial package.
