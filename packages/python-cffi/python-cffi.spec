%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name cffi

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code

License:        MIT
URL:            http://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pycparser
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  libffi-devel
BuildRequires:  gcc

Requires:       python%{python3_pkgversion}-pycparser

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
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
%doc README.md
%exclude %{_bindir}/cffi-gen-src
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/_cffi_backend.cpython-3*-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Aug 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.1-1
- Update to 2.1.1

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.1.0-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.0-1
- Update to 2.1.0
- Remove PEP 639 license-files field incompatible with RHEL 9 setuptools
- Exclude /usr/bin/cffi-gen-src (new binary in 2.1.0, not needed)

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.0-1
- Update to 2.0.0
- Fix PEP 639 license field incompatibility with RHEL 9 setuptools
- Drop stale Requires: setuptools (no longer a runtime dependency)

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 1.17.1-2
- Rebuild against python3.12

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.1-1
- Update to 1.17.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.15.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.15.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.15.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.15.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 1.15.1-1
- Update to 1.15.1

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 1.15.0-2
- Rebuild Against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 1.15.0-1
- Release python-cffi 1.15.0

* Wed Sep 08 2021 Evgeni Golov - 1.14.5-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 1.14.5-1
- Update to 1.14.5

* Mon Sep 28 2020 Evgeni Golov 1.14.3-1
- Update to 1.14.3

* Tue Sep 01 2020 Evgeni Golov 1.14.2-1
- Update to 1.14.2

* Mon Aug 10 2020 Evgeni Golov 1.14.1-1
- Update to 1.14.1

* Wed Mar 18 2020 Samir Jha 1.14.0-1
- Update to 1.14.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.13.2-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.13.2-1
- Initial package.
