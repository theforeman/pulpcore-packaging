%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name typing-extensions

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.16.0
Release:        2%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3

License:        PSF
URL:            https://github.com/python/typing/blob/master/typing_extensions/README.rst
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/typing_extensions-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description
%{summary}


%prep
set -ex
%autosetup -n typing_extensions-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/__pycache__/typing_extensions.*
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/typing_extensions-%{version}.dist-info/


%changelog
* Fri Jul 24 2026 Odilon Sousa <osousa@redhat.com> - 4.16.0-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.16.0-1
- Update to 4.16.0

* Sun Jan 18 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.15.0-1
- Update to 4.15.0

* Sun Jul 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.14.1-1
- Update to 4.14.1

* Sun Jun 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.14.0-1
- Update to 4.14.0

* Sun Apr 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.13.2-1
- Update to 4.13.2

* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 4.12.2-2
- Rebuild against python3.12

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.12.2-1
- Update to 4.12.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.7.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.7.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.7.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.7.1-2
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 4.7.1-1
- Release python-typing-extensions 4.7.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.10.0.2-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.10.0.2-1
- Release python-typing-extensions 3.10.0.2

* Fri Sep 10 2021 Evgeni Golov - 3.7.4.3-3
- Don't require typing, our Python is new enough

* Wed Sep 08 2021 Evgeni Golov - 3.7.4.3-2
- Build against Python 3.8

* Tue Sep 01 2020 Evgeni Golov 3.7.4.3-1
- Update to 3.7.4.3

* Tue Apr 14 2020 Evgeni Golov 3.7.4.2-1
- Update to 3.7.4.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.4.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.7.4.1-1
- Initial package.
