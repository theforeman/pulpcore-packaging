%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name whitenoise

Name:           python-%{pypi_name}
Version:        6.6.0
Release:        1%{?dist}
Summary:        Radically simplified static file serving for WSGI applications

License:        MIT
URL:            https://whitenoise.evans.io
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.6.0-1
- Update to 6.6.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 6.0.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 6.0.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 6.0.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.0.0-2
- Build against python 3.11

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 6.0.0-1
- Release python-whitenoise 6.0.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.3.0-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov 5.3.0-1
- Update to 5.3.0

* Mon Sep 06 2021 Evgeni Golov - 5.2.0-2
- Build against Python 3.8

* Tue Aug 25 2020 Evgeni Golov 5.2.0-1
- Update to 5.2.0

* Thu Jun 04 2020 Evgeni Golov 5.1.0-1
- Update to 5.1.0

* Wed Mar 18 2020 Samir Jha 5.0.1-1
- Update to 5.0.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 4.1.4-1
- Initial package.
