%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.17.2
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            https://www.django-rest-framework.org/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-django >= 4.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}



%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 metadata for the older setuptools available on RHEL
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/rest_framework
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Sep  3 21:39:52 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.17.2-1
- Update to 3.17.2
- Switch to the pyproject wheel build
- Patch PEP 639 metadata for RHEL setuptools compatibility
- Adjust the file list for the wheel contents

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 3.16.1-2
- Bump release for EL10 rebuild

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.16.1-1
- Update to 3.16.1

* Mon Apr 07 2025 Odilon Sousa <osousa@redhat.com> - 3.15.2-3
- Add obsoletes for python3.11 package

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 3.15.2-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.15.2-1
- Update to 3.15.2

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.15.1-1
- Update to 3.15.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.14.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.14.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.14.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.14.0-1
- Update to 3.14.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.13.1-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 3.13.1-1
- Release python-djangorestframework 3.13.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.12.4-5
- Build against python 3.9

* Tue Oct 19 2021 Evgeni Golov - 3.12.4-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Thu Sep 09 2021 Evgeni Golov - 3.12.4-3
- Correct django-rest-framework Provides to mention Python 3.8

* Wed Sep 08 2021 Evgeni Golov - 3.12.4-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov 3.12.4-1
- Update to 3.12.4

* Mon Jan 11 2021 Evgeni Golov 3.12.2-1
- Update to 3.12.2

* Mon Dec 21 2020 Evgeni Golov - 3.12.1-2
- Add provides for python3-django-rest-framework

* Mon Nov 02 2020 Evgeni Golov 3.12.1-1
- Update to 3.12.1

* Thu Oct 29 2020 Evgeni Golov 3.11.2-1
- Update to 3.11.2

* Mon Sep 28 2020 Evgeni Golov 3.11.1-1
- Update to 3.11.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.10.3-1
- Initial package.
