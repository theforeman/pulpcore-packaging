%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-api-core

Name:           python-%{pypi_name}
Version:        2.20.0
Release:        1%{?dist}
Summary:        Google API client core library

License:        Apache 2.0
URL:            https://github.com/googleapis/python-api-core
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_api_core-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Conflicts:      python%{python3_pkgversion}-protobuf = 3.20
Conflicts:      python%{python3_pkgversion}-protobuf = 3.20.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.2
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.3
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.4
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.5
Requires:       python%{python3_pkgversion}-google-auth < 3
Requires:       python%{python3_pkgversion}-google-auth >= 2.14.1
Requires:       python%{python3_pkgversion}-googleapis-common-protos < 2
Requires:       python%{python3_pkgversion}-googleapis-common-protos >= 1.56.2
Requires:       python%{python3_pkgversion}-proto-plus < 2
Requires:       python%{python3_pkgversion}-proto-plus >= 1.22.3
Requires:       python%{python3_pkgversion}-protobuf < 6
Requires:       python%{python3_pkgversion}-protobuf >= 3.19.5
Requires:       python%{python3_pkgversion}-requests < 3
Requires:       python%{python3_pkgversion}-requests >= 2.18


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n google_api_core-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
set -ex
%py3_build



%install
set -ex
%py3_install



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/google_api_core-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.20.0-1
- Initial package.
