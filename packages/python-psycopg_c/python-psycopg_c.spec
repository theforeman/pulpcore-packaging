%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg_c
%global debug_package %{nil}

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.3.3
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python - C extension

License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
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
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
# Relax setuptools version pin (RHEL 9 has setuptools 68.x, not 80.x)
sed -i 's/setuptools == 80\.[0-9.]*/setuptools >= 40/' pyproject.toml
# Remove [[tool.setuptools.ext-modules]] array-of-tables entries (unsupported by setuptools 68.x)
python3 -c "
lines = open('pyproject.toml').readlines()
result = []
skip = False
for line in lines:
    s = line.strip()
    if s == '[[tool.setuptools.ext-modules]]':
        skip = True
    elif skip and s.startswith('[') and s != '[[tool.setuptools.ext-modules]]':
        skip = False
    if not skip:
        result.append(line)
open('pyproject.toml', 'w').writelines(result)
"


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.3-1
- Update to 3.3.3
- Switch to pyproject_wheel (setup.py removed in 3.3.x)
- Fix %files: use dist-info instead of egg-info
- Fix PEP 639 license field and relax setuptools pin for RHEL 9
- Suppress debug_package (no C extension compiled; ext-modules removed for setuptools 68.x)

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
