%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name PyGObject
%global srcname pygobject

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.42.0
Release:        1%{?dist}
Summary:        Python bindings for GObject Introspection

License:        GNU LGPL
URL:            https://pygobject.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pycairo >= 1.16.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

BuildRequires:  cairo-gobject-devel
BuildRequires:  gobject-introspection-devel

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name} = %{version}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pycairo >= 1.16.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license docs/images/LICENSE
%doc .gitlab-ci/README.rst README.rst
%{python3_sitearch}/gi
%{python3_sitearch}/pygtkcompat
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_libdir}/pkgconfig/pygobject-3.0.pc
%{_includedir}/pygobject-3.0


%changelog
* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.42.0-1
- Release python-pygobject 3.42.0

* Mon Sep 13 2021 Evgeni Golov - 3.40.1-1
- Initial package.
