# Created by pyp2rpm-3.3.3
%global pypi_name lxml

Name:           python-%{pypi_name}
Version:        4.6.3
Release:        1%{?dist}
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API

License:        BSD
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
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i '/Cython/d' requirements.txt

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSES.txt doc/licenses/ZopePublicLicense.txt
%doc README.rst src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 11 2021 Evgeni Golov - 4.6.3-1
- Initial package.
