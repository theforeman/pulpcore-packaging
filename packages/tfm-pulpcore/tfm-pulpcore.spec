%global __python /usr/bin/python3
%global scl_vendor theforeman
%global _scl_prefix /opt/%{scl_vendor}
%{!?scl_vendor_in_name: %global scl_vendor_in_name 0}
%global scl_name_prefix tfm-
%global scl_name_base pulpcore
%global scl %{scl_name_prefix}%{scl_name_base}

%scl_package %scl

%global scl_python rh-python38
%global scl_prefix_python %{scl_python}-

%global pulpcore_sitelib %(echo %{python38python3_sitelib} | sed 's|/opt/rh/|%{_scl_prefix}/|;s|%{scl_python}|%{scl}|')
%global pulpcore_sitearch %(echo %{python38python3_sitearch} | sed 's|/opt/rh/|%{_scl_prefix}/|;s|%{scl_python}|%{scl}|')

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
Requires: %{scl_prefix_python}scldevel
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
Provides: %{scl_prefix}python3-setuptools = 41.6.0
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
. scl_source enable %{scl_python}
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
export PYTHONPATH="%{pulpcore_sitelib}:%{pulpcore_sitearch}:\${PYTHONPATH:+:\${PYTHONPATH}}"
EOF
%scl_install

mkdir -p %{buildroot}%{pulpcore_sitelib}
mkdir -p %{buildroot}%{pulpcore_sitearch}

# additional rpm macros for builds in the collection to set the vendor correctly
cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config << EOF
%%scl_vendor %{scl_vendor}
%%_scl_prefix %{_scl_prefix}
%%scl_package_override() %%{expand:%{?python38_os_install_post:%global __os_install_post %python38_os_install_post}
%%global __python_requires %%python38_python_requires
%%global __python_provides %%python38_python_provides
# macros commonly used in specfiles
%%global __python3 %%python38__python3
%%global __python %%python38__python3
%%global python3_version %%python38python3_version
%%global python3_version_nodots %%python38python3_version_nodots
%%global python3_platform %%python38python3_platform
%%global py3dir %%python38py3dir
%%global py3_build %%python38py3_build
%%global py3_build_egg %%python38py3_build_egg
%%global py3_build_wheel %%python38py3_build_wheel
%%global py3_install_egg %%python38py3_install_egg
%%global py3_install_wheel() %%%%{expand:%%{python38py3_install_wheel_start}%%%%{1}%%{python38py3_install_wheel_end}}
%%global python3_sitelib %pulpcore_sitelib
%%global python3_sitearch %pulpcore_sitearch
%%global pulpcorepy3_install() %%{expand:\\\\\\
  %%{?scl:scl enable rh-python38 '}\\\\\\
  CFLAGS="\${CFLAGS:-\${RPM_OPT_FLAGS}}" LDFLAGS="\${LDFLAGS:-\${RPM_LD_FLAGS}}"\\\\\\
  %%{python38__python3} %%{python38py_setup} %%{?py_setup_args} install -O1 --skip-build --root %%{buildroot} --install-purelib %%{python3_sitelib} --install-platlib %%{python3_sitearch} --install-scripts %%{_bindir} %%{?*}\\\\\\
  %%{?scl:'}
}
%%global py3_install %%pulpcorepy3_install
}
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
%pulpcore_sitearch
%pulpcore_sitelib
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
