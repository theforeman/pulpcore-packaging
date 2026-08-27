%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-auth

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.57.0
Release:        1%{?dist}
Summary:        Google Authentication Library

License:        Apache 2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_auth-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-cryptography >= 38.0.3
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
* Thu Aug 27 11:20:28 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.57.0-1
- Update to 2.57.0

* Sun Aug 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.56.3-1
- Update to 2.56.3

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.55.2-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.55.2-1
- Update to 2.55.2

* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.55.1-1
- Update to 2.55.1

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.53.0-1
- Update to 2.53.0
- Add cryptography >= 38.0.3 runtime dependency (required by upstream 2.53.0)

* Sun May 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.52.0-1
- Update to 2.52.0

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.50.0-1
- Update to 2.50.0

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.49.2-1
- Update to 2.49.2

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.49.1-1
- Update to 2.49.1

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
