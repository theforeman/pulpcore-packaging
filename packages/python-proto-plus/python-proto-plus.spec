%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name proto-plus

Name:           python-%{pypi_name}
Version:        1.24.0
Release:        1%{?dist}
Summary:        Beautiful, Pythonic protocol buffers.

License:        Apache 2.0
URL:            https://github.com/googleapis/proto-plus-python
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-protobuf >= 3.19.0
Requires:       python%{python3_pkgversion}-protobuf < 6


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/proto
%{python3_sitelib}/proto_plus-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Odilon Sousa - 1.24.0-1
- Initial package.
