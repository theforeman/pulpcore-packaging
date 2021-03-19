# Created by pyp2rpm-3.3.3
%global pypi_name pycryptodomex

Name:           python-%{pypi_name}
Version:        3.10.1
Release:        1%{?dist}
Summary:        Cryptographic library for Python

License:        BSD, Public Domain
URL:            https://www.pycryptodome.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license Doc/LEGAL/copy/LICENSE.libtom Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/ocb/license1.pdf Doc/ocb/license2.pdf Doc/ocb/license3.pdf Doc/src/license.rst LICENSE.rst
%doc Doc/ocb/README.txt README.rst
%{python3_sitearch}/Cryptodome
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 3.10.1-1
- Update to 3.10.1

* Mon Jul 20 2020 Evgeni Golov 3.9.8-1
- Update to 3.9.8

* Wed Mar 18 2020 Samir Jha 3.9.7-1
- Update to 3.9.7

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.9.6-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 3.9.6-1
- Update to 3.9.6

* Tue Nov 19 2019 Evgeni Golov - 3.9.4-1
- Initial package.
