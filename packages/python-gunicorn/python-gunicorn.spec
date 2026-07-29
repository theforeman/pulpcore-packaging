%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name gunicorn

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        25.1.0
Release:        2%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        MIT
URL:            https://gunicorn.org
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-packaging

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/g' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/gunicorn
%{_bindir}/gunicornc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 25.1.0-2
- Bump release for EL10 rebuild

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 25.1.0-1
- Update to 25.1.0

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 23.0.0-3
- Add obsoletes for python3.11 package

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 23.0.0-2
- Rebuild against python3.12

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 23.0.0-1
- Update to 23.0.0

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 22.0.0-1
- Release python-gunicorn 22.0.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 20.1.0-8
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 20.1.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 20.1.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 20.1.0-1
- Update to 20.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.0.4-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 20.0.4-1
- Update to 20.0.4

* Mon Nov 18 2019 Evgeni Golov - 20.0.0-1
- Initial package.
