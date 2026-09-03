%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg_c

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.3.5
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python - C extension

License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Fix-RHEL-9-10-setuptools-ext-modules-incompatibility.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.37
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  gcc
BuildRequires:  postgresql-devel

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Sep  3 21:40:07 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.5-1
- Update to 3.3.5

* Thu Aug 27 2026 Odilon Sousa <osousa@redhat.com> - 3.3.4-1
- Update to 3.3.4, needed for pulpcore 3.105.17's psycopg_c>=3.3.4,<3.4
- Switch to %%pyproject_wheel/%%pyproject_install: upstream 3.3.4 dropped setup.py
  in favor of a pyproject.toml-only build (custom cython_backend, builds from the
  bundled .c sources so Cython isn't actually invoked from the sdist)
- Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
- Add Patch0: strip [tool.setuptools.ext-modules] from pyproject.toml (RHEL 9/10
  setuptools rejects this still-experimental upstream schema key) and reintroduce
  a setup.py declaring the same packages/ext-modules/cmdclass config classically

* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 3.2.13-2
- Bump release for EL10 rebuild

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.13-1
- Update to 3.2.13

* Sun Sep 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.10-1
- Update to 3.2.10

* Sun Jun 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.9-1
- Update to 3.2.9

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.5-1
- Update to 3.2.5

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 3.2.3-2
- Rebuild against python3.12

* Wed Oct 09 2024 Evgeni Golov - 3.2.3-1
- Initial package.
