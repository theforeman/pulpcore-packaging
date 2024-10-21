%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name isodate

Name:           python-%{pypi_name}
Version:        0.7.2
Release:        1%{?dist}
Summary:        An ISO 8601 date/time/duration parser and formatter

License:        BSD
URL:            https://github.com/gweis/isodate/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  zlib-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
ISO 8601 date/time parser This module implements ISO 8601 date, time and
duration parsing.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
ISO 8601 date/time parser This module implements ISO 8601 date, time and
duration parsing.



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
* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.2-1
- Update to 0.7.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.6.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.6.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.6.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.6.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.6.0-2
- Build against python 3.9

* Tue Nov 02 2021 Evgeni Golov - 0.6.0-1
- Initial package.
