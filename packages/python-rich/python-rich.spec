%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name rich

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        14.3.4
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

License:        MIT
URL:            https://github.com/Textualize/rich
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-markdown-it-py >= 2.1
Requires:       python%{python3_pkgversion}-markdown-it-py < 3
Requires:       python%{python3_pkgversion}-pygments < 3.0.0
Requires:       python%{python3_pkgversion}-pygments >= 2.6.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 14.3.4-1
- Update to 14.3.4

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 14.3.3-1
- Update to 14.3.3
- Switch to pyproject build (setup.py removed upstream, uses poetry-core)
- Fix PEP 639 license format for RHEL9 pip compatibility

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 13.3.1-11
- Add obsoletes for python3.11 package

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 13.3.1-10
- Update dependencies requirement

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 13.3.1-9
- Bump python-rich against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 13.3.1-8
- Remove SCL bits

* Fri Dec 15 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-7
- Obsolete python39-rich for a smooth upgrade

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 13.3.1-6
- Rollback overzealous obsoletes

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-5
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-4
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-3
- Remove typing-extension requirement

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 13.3.1-2
- Disable auto dependency generator

* Fri Feb 03 2023 Odilon Sousa 13.3.1-1
- Update to 13.3.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 10.12.0-3
- Obsolete the old Python 3.9 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 10.12.0-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 10.12.0-1
- Release python-rich 10.12.0

* Wed Oct 20 2021 Evgeni Golov - 10.0.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 10.0.1-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov 10.0.1-1
- Update to 10.0.1

* Thu Nov 05 2020 Evgeni Golov - 6.1.1-2
- Fix License tag in spec file

* Wed Sep 09 2020 Evgeni Golov 6.1.1-1
- Update to 6.1.1

* Tue Sep 01 2020 Evgeni Golov 6.0.0-1
- Update to 6.0.0

* Tue Aug 25 2020 Evgeni Golov - 5.2.1-1
- Initial package.
