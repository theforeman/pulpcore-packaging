%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.10
%global pypi_name google-resumable-media

Name:           python-%{pypi_name}
Version:        2.7.2
Release:        1%{?dist}
Summary:        Utilities for Google Media Downloads and Resumable Uploads

License:        Apache 2.0
URL:            https://github.com/googleapis/google-resumable-media-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_resumable_media-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-google-crc32c < 2
Requires:       python%{python3_pkgversion}-google-crc32c >= 1

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n google_resumable_media-%{version}
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
%{python3_sitelib}/google_resumable_media-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.7.2-1
- Initial package.
