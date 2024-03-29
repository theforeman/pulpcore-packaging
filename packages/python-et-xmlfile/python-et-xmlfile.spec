%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name et-xmlfile

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        6%{?dist}
Summary:        An implementation of lxml.xmlfile for the standard library

License:        MIT
URL:            https://foss.heptapod.net/openpyxl/et_xmlfile
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/et_xmlfile-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n et_xmlfile-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitelib}/et_xmlfile
%{python3_sitelib}/et_xmlfile-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.1.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.1.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.1.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.1.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.1.0-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 1.1.0-1
- Update to 1.1.0

* Mon Sep 06 2021 Evgeni Golov - 1.0.1-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov - 1.0.1-1
- Initial package.
