%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name lxml

Name:           python-%{pypi_name}
Version:        4.9.2
Release:        5%{?dist}
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API

License:        BSD-3-Clause
URL:            https://lxml.de/
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel


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
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i '/Cython/d' requirements.txt


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSES.txt doc/licenses/BSD.txt
%doc README.rst src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.9.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.9.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.9.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.9.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 4.9.2-1
- Update to 4.9.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.7.1-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 4.7.1-1
- Release python-lxml 4.7.1

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 4.6.4-1
- Release python-lxml 4.6.4

* Mon Sep 06 2021 Evgeni Golov - 4.6.3-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov - 4.6.3-1
- Initial package.
