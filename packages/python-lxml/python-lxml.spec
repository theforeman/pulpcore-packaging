%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name lxml

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.7.1
Release:        1%{?dist}
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API

License:        BSD
URL:            https://lxml.de/
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-BeautifulSoup4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-Cython >= 0.29.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cssselect >= 0.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-html5lib
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-BeautifulSoup4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Cython >= 0.29.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cssselect >= 0.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-html5lib


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt LICENSES.txt
%doc README.rst src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 4.7.1-1
- Update to 4.7.1

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 4.6.4-1
- Release python-lxml 4.6.4

* Mon Sep 06 2021 Evgeni Golov - 4.6.3-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov - 4.6.3-1
- Initial package.
