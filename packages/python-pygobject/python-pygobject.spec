%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name PyGObject
%global srcname pygobject

Name:           python-%{srcname}
Version:        3.40.1
Release:        7%{?dist}
Epoch:          1
Summary:        Python bindings for GObject Introspection

License:        GNU LGPL
URL:            https://pygobject.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pycairo >= 1.16.0
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildRequires:  cairo-gobject-devel
BuildRequires:  gobject-introspection-devel

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}
Requires:       python%{python3_pkgversion}-pycairo >= 1.16.0
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{srcname} < %{epoch}:%{version}-%{release}
Obsoletes:      python39-%{srcname} < %{epoch}:%{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


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


%files -n python%{python3_pkgversion}-%{srcname}
%license docs/images/LICENSE
%doc .gitlab-ci/README.rst README.rst
%{python3_sitearch}/gi
%{python3_sitearch}/pygtkcompat
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_libdir}/pkgconfig/pygobject-3.0.pc
%{_includedir}/pygobject-3.0


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1:3.40.1-7
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1:3.40.1-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1:3.40.1-5
- Build against python 3.11

* Tue Oct 04 2022 Odilon Sousa <osousa@redhat.com> - 1:3.40.1-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1:3.40.1-3
- Build against python 3.9

* Tue Jan 25 2022 Evgeni Golov - 1:3.40.1-2
- Bump epoch, there was a 3.42 version in the repo and users might have installed that.

* Mon Sep 13 2021 Evgeni Golov - 3.40.1-1
- Initial package.
