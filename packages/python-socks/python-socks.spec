%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name python_socks
%global srcname socks

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://github.com/romis2012/python-socks
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros



%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description
%{summary}



%package -n python%{python3_pkgversion}-%{srcname}+asyncio
Summary: Metapackage for python%{python3_pkgversion}-%{srcname}: asyncio extra

%description -n python%{python3_pkgversion}-%{srcname}+asyncio
This is a metapackage bringing in filecache extra requires for python%{python3_pkgversion}-%{srcname}
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{srcname}+asyncio
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i "s/^license = '\(.*\)'/license = {text = \"\1\"}/" pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Aug 27 2026 Odilon Sousa <osousa@redhat.com> - 3.0.0-1
- Update to 3.0.0
- Fix PEP 639 license field: upstream 3.0.0 switched to SPDX string format
  (license = 'Apache-2.0'), which RHEL 9/10 setuptools cannot parse; sed-patch
  to the table form in the prep script like other packages in this repo

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.8.2-3
- Bump release for EL10 rebuild

* Mon Jul 20 2026 Zach Huntington-Meath <zhunting@redhat.com> - 2.8.2-2
- Drop async-timeout requirement from +asyncio subpackage

* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.2-1
- Update to 2.8.2

* Sun Mar 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.1-1
- Update to 2.8.1

* Mon Jan 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.0-1
- Update to 2.8.0

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.3-1
- Update to 2.7.3

* Fri Aug 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.2-1
- Update to 2.7.2

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 2.7.1-2
- Rebuild against python3.12

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.1-1
- Update to 2.7.1

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jan 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.6.1-1
- Update to 2.6.1

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.3-1
- Update to 2.5.3

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.2-1
- Update to 2.5.2

* Tue Sep 10 2024 Odilon Sousa <osousa@redhat.com> - 2.5.1-1
- Release python-socks 2.5.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.0.3-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.0.3-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.0.3-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.0.3-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.3-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.0.3-1
- Release python-socks 2.0.3

* Mon Sep 06 2021 Evgeni Golov - 1.2.4-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 1.2.4-1
- Initial package.
