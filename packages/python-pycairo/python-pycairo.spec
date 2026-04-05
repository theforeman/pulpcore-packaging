%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pycairo

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.29.0
Release:        1%{?dist}
Summary:        Python interface for cairo

License:        LGPL-2.1-only OR MPL-1.1
URL:            https://pycairo.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  cairo-devel

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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


%build
set -ex
%meson -Dpython=%{__python3}
%meson_build


%install
set -ex
%meson_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc README.rst
%{python3_sitearch}/cairo
%{python3_sitearch}/%{pypi_name}*.dist-info/


%files -n python%{python3_pkgversion}-%{pypi_name}-devel
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc


%changelog
* Sun Apr 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.29.0-1
- Update to 1.29.0
- Switch to meson build (setup.py removed in 1.29.0)

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 1.20.1-8
- Rebuild against python3.12

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
