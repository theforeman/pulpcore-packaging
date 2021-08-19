%global __python /usr/bin/python3
%global scl_name_prefix tfm-
%global scl_name_base pulpcore
%global scl %{scl_name_prefix}%{scl_name_base}

%scl_package %scl

%global scl_python rh-python38
%global scl_prefix_python %{scl_python}-

%global install_scl 1

# Do not produce empty debuginfo package.
%global debug_package %{nil}

Summary: Package that installs %scl
Name: %scl_name
Version: 1.0
Release: 1%{?dist}
License: GPLv2+
Source1: README
Source2: LICENSE
BuildRequires: help2man
BuildRequires: scl-utils-build
BuildRequires: %{scl_prefix_python}scldevel
BuildRequires: %{scl_prefix_python}python-devel
%if 0%{?install_scl}
Requires: %{scl_python}
%endif

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils
Requires: %{scl_prefix_python}runtime

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build
Requires: %{scl_runtime}
Requires: %{scl_prefix_python}scldevel

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%package scldevel
Summary: Package shipping development files for %scl

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

%package python3-devel
Summary: Empty package pulling in %{scl_prefix_python}python-devel
Requires: %{scl_prefix_python}python-devel

%description python3-devel
Empty package pulling in %{scl_prefix_python}python-devel
This package is only required to ease definition of dependencies inside the SCL

%package python3-setuptools
Summary: Empty package pulling in %{scl_prefix_python}python-setuptools
Requires: %{scl_prefix_python}python-setuptools

%description python3-setuptools
Empty package pulling in %{scl_prefix_python}python-setuptools
This package is only required to ease definition of dependencies inside the SCL

%prep
%setup -T -c

# This section generates README file from a template and creates man page
# from that file, expanding RPM macros in the template file.
cat >README <<'EOF'
%{expand:%(cat %{SOURCE1})}
EOF

# copy the license file so %%files section sees it
cp %{SOURCE2} .

%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_scl_scripts}/root
mkdir -p %{buildroot}%{_root_prefix}/lib/rpm/redhat
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
EOF
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
. scl_source enable %{scl_python}
EOF

# Create the scldevel subpackage macros

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF


# install generated man page
mkdir -p %{buildroot}%{_mandir}/man7/
install -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/%{scl_name}.7

%files

%files runtime -f filesystem
%doc README LICENSE
%scl_files
%{_mandir}/man7/%{scl_name}.*

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%files python3-devel

%files python3-setuptools

%changelog
* Tue Aug 17 2021 Evgeni Golov - 1.0-1
- Initial package.
