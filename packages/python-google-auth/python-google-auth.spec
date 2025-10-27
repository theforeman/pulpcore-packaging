%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-auth

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.41.1
Release:        2%{?dist}
Summary:        Google Authentication Library

License:        Apache 2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_auth-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-cachetools < 7
Requires:       python%{python3_pkgversion}-cachetools >= 2
Requires:       python%{python3_pkgversion}-pyasn1-modules >= 0.2.1
Requires:       python%{python3_pkgversion}-rsa < 5
Requires:       python%{python3_pkgversion}-rsa >= 3.1.4

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n google_auth-%{version}
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
%{python3_sitelib}/google_auth-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 27 2025 Odilon Sousa <osousa@redhat.com> - 2.41.1-2
- Allow new cachetools

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.41.1-1
- Update to 2.41.1

* Sun Jun 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.40.3-1
- Update to 2.40.3

* Sun May 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.40.2-1
- Update to 2.40.2

* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.40.1-1
- Update to 2.40.1

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.39.0-1
- Update to 2.39.0

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.38.0-2
- Rebuild against python3.12

* Mon Jan 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.38.0-1
- Update to 2.38.0

* Wed Dec 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.37.0-1
- Update to 2.37.0

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.36.0-1
- Update to 2.36.0

* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 2.35.0-1
- Initial package.
