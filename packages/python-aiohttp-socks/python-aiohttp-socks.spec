%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-socks

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.12.0
Release:        1%{?dist}
Summary:        Proxy connector for aiohttp

License:        Apache 2
URL:            https://github.com/romis2012/aiohttp-socks
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/aiohttp_socks-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-aiohttp >= 2.3.2
Requires:       python%{python3_pkgversion}-socks < 4.0.0
Requires:       python%{python3_pkgversion}-socks >= 2.4.3

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n aiohttp_socks-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/aiohttp_socks
%{python3_sitelib}/aiohttp_socks-%{version}.dist-info/


%changelog
* Thu Aug 27 2026 Odilon Sousa <osousa@redhat.com> - 0.12.0-1
- Update to 0.12.0
- Fix PEP 639 license field: upstream 0.12.0 switched to SPDX string format
  (license = "Apache-2.0"), which RHEL 9/10 setuptools cannot parse
- Relax socks upper bound to < 4.0.0 (upstream 0.12.0 allows python-socks<4.0.0,
  needed to unblock python-socks 3.0.0)

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 0.10.1-2
- Bump release for EL10 rebuild

* Sun Jun 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.1-1
- Update to 0.10.1

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 0.8.4-2
- Rebuild against python3.12

* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.8.4-1
- Update to 0.8.4

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.7.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.7.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.7.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.7.1-4
- Build against python 3.11

* Fri May 06 2022 Odilon Sousa <osousa@redhat.com> - 0.7.1-3
- Rebuilding with python_disable_dependency_generator macro

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.7.1-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa 0.7.1-1
- Update to 0.7.1

* Mon Sep 06 2021 Evgeni Golov - 0.6.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 0.6.0-1
- Initial package.
