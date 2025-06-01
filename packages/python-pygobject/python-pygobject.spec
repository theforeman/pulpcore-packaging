%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name PyGObject
%global srcname pygobject

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.50.1
Release:        1%{?dist}
Epoch:          1
Summary:        Python bindings for GObject Introspection

License:        GNU LGPL
URL:            https://pygobject.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-meson-python
BuildRequires:  python%{python3_pkgversion}-pycairo >= 1.16.0
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


BuildRequires:  cairo-gobject-devel
BuildRequires:  gobject-introspection-devel

Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}
Requires:       python%{python3_pkgversion}-pycairo >= 1.16.0

Obsoletes:      python3.11-%{srcname} < %{version}-%{release}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%{_includedir}/python%{python3_pkgversion}/%{srcname}/pygobject-3.0
%{python3_sitearch}/gi
%{python3_sitearch}/pygtkcompat
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Sun Jun 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.50.1-1
- Update to 3.50.1

* Sun May 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.50.0-1
- Update to 3.50.0

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 1:3.48.2-2
- Add obsoletes for python3.11 package

* Fri Apr 04 2025 Odilon Sousa <osousa@redhat.com> - 1:3.48.2-1
- Release python-pygobject 3.48.2

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 1:3.40.1-8
- Rebuild against python3.12

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
