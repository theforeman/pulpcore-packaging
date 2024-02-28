%global libname solv

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

%bcond_without python_bindings

# Creates special prefixed pseudo-packages from appdata metadata
%bcond_without appdata

# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
%bcond_without conda

# For rich dependencies
%bcond_without complex_deps

%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo

# For handling deb + rpm at the same time
%bcond_without multi_semantics
%bcond_with zchunk

%bcond_without zstd

%define __cmake_switch(b:) %{expand:%%{?with_%{-b*}:ON}}%{expand:%%{!?with_%{-b*}:OFF}}

Name:           python-%{libname}
Version:        0.7.28
Release:        1%{?dist}
Summary:        Python bindings for the lib%{libname} library

License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source:         %{url}/archive/%{version}/lib%{libname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel


BuildRequires:  swig
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

# -DWITH_LIBXML2=ON
BuildRequires:  libxml2-devel

# -DWITH_OPENSSL=ON
BuildRequires:  pkgconfig(openssl)

# -DENABLE_LZMA_COMPRESSION=ON
BuildRequires:  xz-devel

# -DENABLE_BZIP2_COMPRESSION=ON
BuildRequires:  bzip2-devel

%if %{with zstd}
# -DENABLE_ZSTD_COMPRESSION=ON
BuildRequires:  libzstd-devel
%endif

%if %{with zchunk}
# -DENABLE_ZCHUNK_COMPRESSION=ON
BuildRequires:  libzck-devel
%endif

%description
Python bindings for the %{name} library.

Python 3 version.



%prep
%autosetup -p1 -n lib%{libname}-%{version}

%build
%cmake -GNinja                                            \
  -DFEDORA=1                                              \
  -DENABLE_RPMDB=ON                                       \
  -DENABLE_RPMDB_BYRPMHEADER=ON                           \
  -DENABLE_RPMDB_LIBRPM=ON                                \
  -DENABLE_RPMPKG_LIBRPM=ON                               \
  -DENABLE_RPMMD=ON                                       \
  -DENABLE_COMPS=%{__cmake_switch -b comps}               \
  -DENABLE_APPDATA=%{__cmake_switch -b appdata}           \
  -DUSE_VENDORDIRS=ON                                     \
  -DWITH_LIBXML2=ON                                       \
  -DWITH_OPENSSL=ON                                       \
  -DENABLE_LZMA_COMPRESSION=ON                            \
  -DENABLE_BZIP2_COMPRESSION=ON                           \
  -DENABLE_ZSTD_COMPRESSION=%{__cmake_switch -b zstd}     \
  -DENABLE_ZCHUNK_COMPRESSION=%{__cmake_switch -b zchunk} \
%if %{with zchunk}
  -DWITH_SYSTEM_ZCHUNK=ON                                 \
%endif
  -DENABLE_HELIXREPO=%{__cmake_switch -b helix_repo}      \
  -DENABLE_SUSEREPO=%{__cmake_switch -b suse_repo}        \
  -DENABLE_DEBIAN=%{__cmake_switch -b debian_repo}        \
  -DENABLE_ARCHREPO=%{__cmake_switch -b arch_repo}        \
  -DMULTI_SEMANTICS=%{__cmake_switch -b multi_semantics}  \
  -DENABLE_COMPLEX_DEPS=%{__cmake_switch -b complex_deps} \
  -DENABLE_CONDA=%{__cmake_switch -b conda}               \
  -DENABLE_PYTHON=%{__cmake_switch -b python_bindings}    \
  -DENABLE_STATIC=ON                                      \
  -DDISABLE_SHARED=ON                                     \
  -DPYTHON_LIBRARY=/usr/lib64/libpython3.11.so.1.0        \
  -DPYTHON_INCLUDE_DIR=/usr/include/python3.11            \
  -DPYTHON_EXECUTABLE=%{python3}                          \
  %{nil}
%cmake_build

%install
%cmake_install


rm -rf %{buildroot}/usr/bin/
rm -rf %{buildroot}/usr/include/
rm -rf %{buildroot}%{_libdir}/debug/
rm -rf %{buildroot}/usr/bin/
rm -rf %{buildroot}%{_datadir}

rm %{buildroot}/usr/lib64/libsolv*.a
rm %{buildroot}/usr/lib64/pkgconfig/libsolv*.pc


%check
%ctest

# Python smoke test (not tested in %%ctest):
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%python3 -c 'import solv'

%package -n     python%{python3_pkgversion}-%{libname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{libname}}

%description -n python%{python3_pkgversion}-%{libname}
%{summary}


%files -n python%{python3_pkgversion}-%{libname}
%license LICENSE*
%doc README
%{python3_sitearch}/_%{libname}.so
%{python3_sitearch}/%{libname}.py
%{python3_sitearch}/__pycache__/%{libname}.*


%changelog
* Tue Feb 27 2024 Patrick Creech <pcreech@redhat.com> - 0.7.28-1
- Build python3 bindings statically linked.
