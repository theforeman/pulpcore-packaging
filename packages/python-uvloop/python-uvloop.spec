%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name uvloop

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Fast implementation of asyncio event loop on top of libuv

License:        MIT OR Apache-2.0
URL:            https://github.com/MagicStack/uvloop/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  pyproject-rpm-macros
BuildRequires:  gcc
BuildRequires:  libuv-devel

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}

# There currently doesn’t appear to be a way to pass through these “build_ext
# options,” so we resort to patching the defaults. Some related discussion
# appears in https://github.com/pypa/setuptools/issues/3896.	
#
# always use cython to generate code (and generate a build dependency on it)
sed -i -e "/self.cython_always/s/False/True/" setup.py
	
# use system libuv
sed -i -e "/self.use_system_libuv/s/False/True/" setup.py

# Patch Cython version
# EL9 ships with 0.29.35
sed -i 's/"Cython([^"]*)"/"Cython"/' pyproject.toml
sed -i "s|^\(CYTHON_DEPENDENCY *= *'\)Cython([^']*)'|\1Cython'|" setup.py 
	
# To be sure, no 3rd-party stuff
rm -vrf vendor/

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

# Don’t ship C sources and headers.
find '%{buildroot}%{python3_sitearch}' -type f -name '*.[ch]' -print -delete

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Apr 22 2025 Odilon Sousa <osousa@redhat.com> - 0.20.0-1
- Initial package.
