%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-resumable-media

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.10.0
Release:        1%{?dist}
Summary:        Utilities for Google Media Downloads and Resumable Uploads

License:        Apache 2.0
URL:            https://github.com/googleapis/google-resumable-media-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_resumable_media-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-google-crc32c < 2
Requires:       python%{python3_pkgversion}-google-crc32c >= 1

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.10.0-1
- Update to 2.10.0

* Sun May 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.9.0-1
- Update to 2.9.0

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.2-1
- Update to 2.8.2

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.0-1
- Update to 2.8.0

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.7.2-2
- Rebuild against python3.12

* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.7.2-1
- Initial package.
