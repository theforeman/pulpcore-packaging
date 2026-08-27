%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.3.4
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python

License:        GNU Lesser General Public License v3 (LGPLv3)
URL:            https://psycopg.org/psycopg3/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.37
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-typing-extensions >= 4.6

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Aug 27 2026 Odilon Sousa <osousa@redhat.com> - 3.3.4-1
- Update to 3.3.4, needed for pulpcore 3.105.17's psycopg>=3.3.4,<3.4
- Switch to %%pyproject_wheel/%%pyproject_install: upstream 3.3.4 dropped setup.py
  in favor of a pure pyproject.toml + setuptools.build_meta build
- Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
- Raise typing-extensions lower bound to >= 4.6 (upstream 3.3.4 requires >= 4.6)

* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 3.2.13-2
- Bump release for EL10 rebuild

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.13-1
- Update to 3.2.13

* Wed Nov 12 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.12-1
- Update to 3.2.12

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.11-1
- Update to 3.2.11

* Sun Sep 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.10-1
- Update to 3.2.10

* Sun Jun 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.9-1
- Update to 3.2.9

* Fri Apr 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.5-1
- Update to 3.2.5

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 3.2.3-2
- Rebuild against python3.12

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.3-1
- Update to 3.2.3

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.1.18-1
- Update to 3.1.18

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.1.9-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.1.9-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.1.9-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.1.9-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa - 3.1.9-1
- Initial package.
