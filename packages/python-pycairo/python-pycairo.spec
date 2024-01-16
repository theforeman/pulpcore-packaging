%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pycairo

Name:           python-%{pypi_name}
Version:        1.20.1
Release:        7%{?dist}
Summary:        Python interface for cairo

License:        LGPL-2.1-only OR MPL-1.1
URL:            https://pycairo.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildRequires:  cairo-devel

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}-devel
Summary:        %{summary} - devel
Requires:       python%{python3_pkgversion}-%{pypi_name}%{?_isa} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{pypi_name}-devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with py3cairo.


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc README.rst
%{python3_sitearch}/cairo
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%files -n python%{python3_pkgversion}-%{pypi_name}-devel
%{_libdir}/pkgconfig/py3cairo.pc
%{_includedir}/pycairo


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.20.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.20.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.20.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.20.1-4
- Build against python 3.11

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 1.20.1-3
- Rebuild against python 3.9

* Wed Nov 24 2021 Evgeni Golov - 1.20.1-2
- Split devel files into own package

* Mon Sep 13 2021 Evgeni Golov - 1.20.1-1
- Initial package.
