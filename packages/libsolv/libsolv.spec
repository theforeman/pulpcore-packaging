%global libname solv

%bcond_without python_bindings
%bcond_without perl_bindings
%bcond_without ruby_bindings
# Creates special prefixed pseudo-packages from appdata metadata
%bcond_without appdata
# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
%bcond_without conda
# For rich dependencies
%bcond_without complex_deps
%if 0%{?rhel}
%bcond_with helix_repo
%bcond_with suse_repo
%bcond_with debian_repo
%bcond_with arch_repo
# For handling deb + rpm at the same time
%bcond_with multi_semantics
%bcond_with zchunk
%else
%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo
# For handling deb + rpm at the same time
%bcond_without multi_semantics
%bcond_without zchunk
%endif
%bcond_without zstd

#global commitnum 2901
#global commit 47fbaa2a0892866d30ec0e1b4c885532d0aca7b8
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

%define __cmake_switch(b:) %{expand:%%{?with_%{-b*}:ON}}%{expand:%%{!?with_%{-b*}:OFF}}

Name:           lib%{libname}
Version:        0.7.20
Release:        6%{?dist}
Epoch:          1
Summary:        Package dependency solver

License:        BSD
URL:            https://github.com/openSUSE/libsolv
%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=1630300
Patch1:         0001-Add-support-for-computing-hashes-using-OpenSSL.patch
Patch2:         0002-Add-support-for-storing-user-data-in-a-solv-file.patch
Patch3:         0003-Allow-accessing-toolversion-at-runtime-and-increase-.patch
Patch4:         0004-Treat-condition-both-as-positive-and-negative-litera.patch
Patch5:         0005-Allow_break_arch_lock_step_on_erase.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel
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
BuildRequires:  pkgconfig(zck)
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=1830346
Conflicts:      rpm%{?_isa} < 4.14.3

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rpm-devel%{?_isa}

%description devel
Development files for %{name}.

%package tools
Summary:        Package dependency solver tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# repo2solv dependencies. Used as execl()
Requires:       /usr/bin/find

%description tools
Package dependency solver tools.

%package demo
Summary:        Applications demoing the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
# solv dependencies. Used as execlp() and system()
Requires:       /usr/bin/curl
Requires:       /usr/bin/gpg2

%description demo
Applications demoing the %{name} library.

%if %{with perl_bindings}
%package -n perl-%{libname}
Summary:        Perl bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  perl-devel
BuildRequires:  perl-generators
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{libname}
Perl bindings for the %{name} library.
%endif

%if %{with ruby_bindings}
%package -n ruby-%{libname}
Summary:        Ruby bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{libname}
Ruby bindings for the %{name} library.
%endif

%if %{with python_bindings}
%package -n python3-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python3-%{libname}}
BuildRequires:  swig
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%prep
%autosetup -p1 %{?commit:-n %{name}-%{commit}}

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
  -DENABLE_PERL=%{__cmake_switch -b perl_bindings}        \
  -DENABLE_RUBY=%{__cmake_switch -b ruby_bindings}        \
  -DENABLE_PYTHON=%{__cmake_switch -b python_bindings}    \
%if %{with python_bindings}
  -DPYTHON_EXECUTABLE=%{python3}                          \
%endif
  %{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

# Python smoke test (not tested in %%ctest):
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%python3 -c 'import solv'

%files
%license LICENSE*
%doc README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}ext.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}ext.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}ext.pc
# Own directory because we don't want to depend on cmake
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/%{name}*.3*

# Some small macro to list tools with mans
%global solv_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*

%files tools
%solv_tool deltainfoxml2solv
%solv_tool dumpsolv
%solv_tool installcheck
%solv_tool mergesolv
%solv_tool repomdxml2solv
%solv_tool rpmdb2solv
%solv_tool rpmmd2solv
%solv_tool rpms2solv
%solv_tool testsolv
%solv_tool updateinfoxml2solv
%solv_tool repo2solv
%if %{with comps}
  %solv_tool comps2solv
%endif
%if %{with appdata}
  %solv_tool appdata2solv
%endif
%if %{with debian_repo}
  %solv_tool deb2solv
%endif
%if %{with arch_repo}
  %solv_tool archpkgs2solv
  %solv_tool archrepo2solv
%endif
%if %{with helix_repo}
  %solv_tool helix2solv
%endif
%if %{with suse_repo}
  %solv_tool susetags2solv
%endif
%if %{with conda}
  %{_bindir}/conda2solv
%endif

%files demo
%solv_tool solv

%if %{with perl_bindings}
%files -n perl-%{libname}
%{perl_vendorarch}/%{libname}.pm
%{perl_vendorarch}/%{libname}.so
%endif

%if %{with ruby_bindings}
%files -n ruby-%{libname}
%{ruby_vendorarchdir}/%{libname}.so
%endif

%if %{with python_bindings}
%files -n python3-%{libname}
%{python3_sitearch}/_%{libname}.so
%{python3_sitearch}/%{libname}.py
%{python3_sitearch}/__pycache__/%{libname}.*
%endif

%changelog
* Mon Jan 22 2024 Patrick Creech <pcreech@redhat.com> - 1:0.7.20-6
- Rebase libsolv and add epoc

* Wed Jun 21 2023 Jaroslav Rohel <jrohel@redhat.com> - 0.7.20-6
- Backport Allow to break arch lock-step on erase operations (RhBug:2172288,2172292)

* Wed May 17 2023 Jaroslav Rohel <jrohel@redhat.com> - 0.7.20-5
- Backport Treat condition both as positive and negative literal in pool_add_pos_literals_complex_dep
  (RhBug:2185061,2190136)

* Wed Dec 07 2022 Nicola Sella <nsella@redhat.com> - 0.7.20-4
- Drop patch to fix pick of old build (RhBug:2150300,RhBug:2151551)

* Thu May 05 2022 Lukas Hrazky <lhrazky@redhat.com> - 0.7.20-3
- Allow accessing toolversion at runtime and increase it

* Wed May 04 2022 Lukas Hrazky <lhrazky@redhat.com> - 0.7.20-2
- Add support for storing user data in a solv file
- Improve choice rule generation

* Tue Nov 09 2021 Pavla Kratochvilova <pkratoch@redhat.com> - 0.7.20-1
- Update to 0.7.20
- new SOLVER_EXCLUDEFROMWEAK job to ignore pkgs for weak dependencies
- support for environments in comps parser
- fix misparsing of '&' in attributes with libxml2
- choice rules: treat orphaned packages as newest
- fix compatibility with Python 3.10

* Tue Jul 27 2021 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.19-1
- Update to 0.7.19
- repo_add_conda: add flag to skip v2 packages
- fix rare segfault in resolve_jobrules() that could happen if new rules are learnt
- fix error handling in solv_xfopen_fd()
- fix memory leaks

* Fri Apr 30 2021 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.17-2
- Fix rpm dependency

* Thu Apr 29 2021 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.17-1
- Update to 0.7.17
- selected bug fixes:
  * repo_write: fix handling of nested flexarray
  * improve choicerule generation a bit more to cover more cases
  * harden testcase parser against repos being added too late
  * support python-3.10
  * check %_dbpath macro in rpmdb code
- new features:
  * handle default/visible/langonly attributes in comps parser
  * support multiple collections in updateinfo parser
  * add '-D' option in rpmdb2solv to set the dbpath

* Thu Jan 14 2021 Nicola Sella <nsella@redhat.com> - 0.7.16-2
- Enable zstd compression in libsolv

* Wed Nov 11 2020 Nicola Sella <nsella@redhat.com> - 0.7.16-1
- Update to 0.7.16
- selected bug fixes:
  * make testcase_mangle_repo_names deal correctly with freed repos
  [bnc#1177238]
  * fix add_complex_recommends() selecting conflicted packages in
    rare cases leading to crashes
  * improve choicerule generation so that package updates are
    prefered in more cases
  * fix deduceq2addedmap clearing bits outside of the map
  * conda: feature depriorization and fix startswith implementation
  * Fix solvable swapping messing up idarrays
  * fix ruleinfo of complex dependencies returning the wrong origin
  * fix solv_zchunk decoding error if large chunks are used
    [bnc#1159314]
- new features
  * new testcase_mangle_repo_names() function
  * new solv_fmemopen() function
  * Enable zstd compression support for sle15 and sle15-sp2
  * Support blacklisted packages in solver_findproblemrule()
    [bnc#1172135]
  * Support rules with multiple negative literals in choice rule
    generation
  * build with -DENABLE_RPMDB_LIBRPM=1 on SUSE to support
    multiple rpm database backends
  * added two new function to make libzypp independent of the rpm
    database format
  * support conda constrains dependencies


* Mon Apr 06 2020 Ales Matej <amatej@redhat.org> - 0.7.11-1
- Update to 0.7.11
- selected bug fixes:
  * support arch<->noarch package changes when creating patch
    conflicts from the updateinfo data
  * also support other rpm database types
  * fixed solv_zchunk decoding error if large chunks are used
  * treat retracted pathes as irrelevant
  * made add_update_target work with multiversion installs
- new features
  * support for SOLVER_BLACKLIST jobs that block the installation of matched
    packages unless they are directly selected by an SOLVER_INSTALL job
  * libsolv now also parses the patch status in the updateinfo parser
  * new solvable_matchessolvable() function
  * support conda constrains dependencies
  * new rpm_stat_database() function
  * new rpm_hash_database_state() function


* Tue Jun 11 2019 Ales Matej <amatej@redhat.org> - 0.7.7-1
- Update to 0.7.7
- selected bug fixes:
  * fix updating of too many packages in focusbest mode
  * fix handling of disabled installed packages in distupgrade
  * fix repository priority handling for multiversion packages
  * better support of inverval deps in pool_match_dep()
  * support src rpms that have non-empty provides
  * fix favorq leaking between solver runs if the solver is reused
  * fix SOLVER_FLAG_FOCUS_BEST updateing packages without reason
  * be more correct with multiversion packages that obsolete their
    own name
  * allow building with swig-4.0.0
  * lock jobs now take precedence over dup and forcebest jobs
- new features
  * new POOL_FLAG_WHATPROVIDESWITHDISABLED pool flag 
  * bindings: add get_disabled_list() and set_disabled_list()
  * bindings: add whatcontainsdep()
  * bindings: make the selection filters return the self object
  * MSVC compilation support

* Tue Jun 11 2019 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.4-3
- Backport patches: Use OpenSSL for computing hashes (RhBug:1630300)

* Wed May 29 2019 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.4-2
- Backport patch: Not considered excluded packages as a best candidate (RhBug:1677583)

* Fri Apr 26 2019 Pavla Kratochvilova <pkratoch@redhat.org> - 0.7.4-1
- soname bump to "1"
- incompatible API changes:
  * bindings: Selection.flags is now an attribute
  * repodata_lookup_num now works like the other lookup_num functions
- new functions:
  * selection_make_matchsolvable
  * selection_make_matchsolvablelist
  * pool_whatmatchessolvable
  * repodata_search_arrayelement
  * repodata_lookup_kv_uninternalized
  * repodata_search_uninternalized
  * repodata_translate_dir
- new repowriter interface to write solv files allowing better
  control over what gets written
- support for filtered file lists with a custom filter
- dropped support of (since a long time unused) REPOKEY_TYPE_U32
- selected bug fixes:
  * fix nasty off-by-one error in repo_write
  * do not autouninstall packages because of forcebest updates
  * fixed a couple of null pointer derefs and potential memory
    leaks
  * made disfavoring recommended packages work if strong recommends
    is enabled
  * no longer disable infarch rules when they don't conflict with
    the job
  * repo_add_rpmdb: do not copy bad solvables from the old solv file
  * fix cleandeps updates not updating all packages
- new features:
  * support rpm's new '^' version separator
  * support set/get_considered_list in bindings
  * new experimental SOLVER_FLAG_ONLY_NAMESPACE_RECOMMENDED flag
  * do favor evaluation before pruning allowing to (dis)favor
    specific package versions
  * bindings: support pool.matchsolvable(), pool.whatmatchessolvable()
    pool.best_solvables() and selection.matchsolvable()
  * experimental DISTTYPE_CONDA and REL_CONDA support

* Fri Feb 08 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.6.35-6
- Backport patch to add support for modular updateinfoxml data

* Wed Feb 06 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.6.35-5
- Backport patches for: Install of update of nss.x86_64 adds i686 into transaction (RhBug:1663136)

* Wed Dec 12 2018 Pavla Kratochvilova <pkratoch@redhat.org> - 0.6.35-4
- Backport patch: Fix memory leaks, memory access, not used values

* Mon Oct 15 2018 Jaroslav Mracek <jmracek@redhat.org> - 0.6.35-3
- Update to 0.6.35
- Backport patch: Make sure that targeted updates don't do reinstalls

* Sun Jun 10 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.6.34-2
- Conditionalize the python2 subpackage

* Mon Mar 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.34-1
- Update to 0.6.34

* Wed Feb 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.33-1
- Update to 0.6.33

* Tue Feb 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.32-1
- Update to 0.6.32

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.31-1
- Update to 0.6.31

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-9.git.2901.47fbaa2
- Use librpm to access rpm headers

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-8.git.2900.8bdcce1
- Use librpm to access DB

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-7.git.2898.ae214a6
- Switch to %%ldconfig_scriptlets

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-6.git.2898.ae214a6
- Disable librpm from accessing DB

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-5.git.2898.ae214a6
- Allow disabling python2 bindings

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-4.git.2898.ae214a6
- Switch to ninja-build

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-3.git.2898.ae214a6
- Update to latest git version
- Switch to use librpm for accessing headers / rpmdb

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-3.git.2887.97b8c0c
- Update to latest snapshot

* Mon Nov 06 2017 Panu Matilainen <pmatilai@redhat.com> - 0.6.30-2
- Better error message on DB_VERSION_MISMATCH errors

* Tue Oct 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.30-1
- Update to 0.6.30

* Tue Sep 19 2017 Panu Matilainen <pmatilai@redhat.com> - 0.6.29-2
- Band-aid for DB_VERSION_MISMATCH errors on glibc updates

* Thu Sep 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.29-1
- Update to 0.6.29

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.28-8
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.28-7
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.28-6
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.28-5
- Add support for REL_WITHOUT

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.28-2
- Backport patch for fixing yumobs

* Sat Jul 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.28-1
- Update to 0.6.28

* Mon May 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.27-2
- Backport few fixes for bindings

* Thu May 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.27-1
- Update to 0.6.27

* Mon Mar 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.26-5.git.20.668e249
- Update to latest snapshot

* Sat Mar 18 2017 Neal Gompa <ngompa13@gmail.com> - 0.6.26-4.git.19.2262346
- Enable AppData support (#1427171)

* Thu Mar 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.26-3.git.19.2262346
- Update to latest git
- Switch to libxml2

* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.26-2
- Use %%{__python3} as PYTHON3_EXECUTABLE

* Wed Feb 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.26-1
- Update to 0.6.26

* Tue Feb 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.25-1
- Update to 0.6.25

* Fri Jan 13 2017 Vít Ondruch <vondruch@redhat.com> - 0.6.24-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.6.24-3
- Rebuild for Python 3.6

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 0.6.24-2
- Use upstream python build options

* Fri Nov 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.24-1
- Update to 0.6.24

* Sat Oct 29 2016 Denis Ollier <larchunix@gmail.com> - 0.6.23-6
- Typo fixes in spec: s/MULTI_SYMANTICS/MULTI_SEMANTICS/

* Tue Sep 13 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.23-5
- Trivial fixes in spec

* Sat Aug 27 2016 Neal Gompa <ngompa13@gmail.com> - 0.6.23-4
- Enable suserepo on Fedora to enable making openSUSE containers with Zypper

* Fri Aug 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.23-3
- Enable helixrepo on Fedora

* Wed Aug 03 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.23-2
- Backport patch to fix dnf --debugsolver crash (RHBZ #1361831)

* Wed Jul 27 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.23-1
- Update to 0.6.23

* Wed Jul 20 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.22-3
- Backport couple of patches from upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.22-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.22-1
- Update to 0.6.22
- Backport patch which will help to not autoremove needed packages
  (RHBZ #1227066, #1284349)

* Mon Jun 06 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.21-3
- Enable deb/arch support for non-rhel distros

* Mon May 30 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.21-2
- Modify enabled/disabled features

* Wed May 18 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.21-1
- Update to 0.6.21

* Tue May 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.20-2
- Backport patch to fix crashing on reading some repos (RHBZ #1318662)
- Backport patch to fix installing multilib packages with weak deps
  (RHBZ #1325471)

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.20-1
- Update to 0.6.20

* Tue Apr 05 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.19-3
- Reorganize spec file
- Enable helixrepo feature
- enable appdata feature

* Tue Mar 8 2016 Jaroslav Mracek <jmracek@redhat.com> - 0.6.19-2
- Apply 9 patches from upstream

* Sat Feb 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.19-1
- Update to 0.6.19

* Tue Feb  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.15-6
- Explicitly add rubypick and ruubygems build dependencies

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.6.15-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Sun Jan 10 2016 Dan Horák <dan[at]danny.cz> - 0.6.15-4
- fix build on non-Fedora with python3

* Tue Jan 05 2016 Jaroslav Mracek <jmracek@redhat.com> - 0.6.15-3
- Fix bz2 compression support for python3 (RhBug:1293652)

* Fri Dec 18 2015 Michal Luscon <mluscon@redhat.com> - 0.6.15-2
- Revert reworked multiversion orphaned handling

* Thu Dec 17 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.15-1
- Update to 0.6.15

* Tue Dec 08 2015 Jaroslav Mracek <jmracek@redhat.com> - 0.6.14-7
- Rebase to upstream b1ea392
- Enable bz2 compression support (Mikolaj Izdebski <mizdebsk@redhat.com>) (RhBug:1226647)

* Thu Nov 26 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-6
- revert obsolete, as %%python_provide does it (undocumented)

* Wed Nov 18 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-5
- adjust obsolete for stupid packaging

* Wed Nov 18 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-4
- python2-solv obsoletes python-solv (#1263230)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 14 2015 Michal Luscon <mluscon@redhat.com> - 0.6.14-2
- Backport patches from upstream

* Mon Oct 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.14-1
- Update to 0.6.14
- Backport patches from upstream

* Thu Sep 10 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.12-1
- Update to 0.6.12

* Wed Aug 05 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-3
- added compile flag to support rich dependencies
- new version adding MIPS support
- Distribute testsolv in -tools subpackage (Igor Gnatenko)
- Enable python3 bindings for fedora (Igor Gnatenko)

* Tue Aug 04 2015 Adam Williamson <awilliam@redhat.com> - 0.6.11-2
- make bindings require the exact matching version of the lib (#1243737)

* Mon Jun 22 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-1
- new version fixing segfault
- RbConfig fixed in the upstream (1928f1a), libsolv-ruby22-rbconfig.patch erased

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.10-1
- new version fixing segfault

* Fri Mar 6 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.8-3
- Rebuilt with new provides selection feature

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Jan 16 2015 Richard Hughes <richard@hughsie.com> - 0.6.8-2
- Update to latest upstream release to fix a crash in PackageKit.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild


* Mon Aug 11 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.4-2
- Rebase to upstream 12af31a

* Mon Jul 28 2014 Aleš Kozumplík <akozumpl@redhat.com> - 0.6.4-1
- Rebase to upstream 5bd9589

* Mon Jul 14 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.4-0.git2a5c1c4
- Rebase to upstream 2a5c1c4
- Filename selector can start with a star

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2.git6d968f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Aleš Kozumplík <ales@redhat.com> - 0.6.1-1.git6d968f1
- Rebase to upstream 6d968f1
- Fix RhBug:1049209

* Fri Apr 25 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.1-0.gitf78f5de
- Rebase to 0.6.0, upstream commit f78f5de.

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 0.6.0-0.git05baf54.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Wed Apr 9 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.0-0.git05baf54
- Rebase to 0.6.0, upstream commit 05baf54.

* Mon Dec 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.1-1.gitbcedc98
- Rebase upstream bcedc98
- Fix RhBug:1051917.

* Mon Dec 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.1-0.gita8e47f1
- Rebase to 0.4.1, upstream commit a8e47f1.

* Fri Nov 22 2013 Zdenek Pavlas <zpavlas@redhat.com> - 0.4.0-2.git4442b7f
- Rebase to 0.4.0, upstream commit 4442b7f.
- support DELTA_LOCATION_BASE for completeness

* Tue Oct 29 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.0-1.gitd49d319
- Rebase to 0.4.0, upstream commit d49d319.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-9.gita59d11d
- Perl 5.18 rebuild

* Wed Jul 31 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-8.gita59d11d
- Rebase to upstream a59d11d.

* Fri Jul 19 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-7.git228d412
- Add build flags, including Deb, Arch, LZMA and MULTI_SEMANTICS. (RhBug:985905)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-6.git228d412
- Perl 5.18 rebuild

* Mon Jun 24 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-5.git228d412
- Rebase to upstream 228d412.
- Fixes hawkey github issue https://github.com/akozumpl/hawkey/issues/13

* Thu Jun 20 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-4.git209e9cb
- Rebase to upstream 209e9cb.
- Package the new man pages.

* Thu May 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-3.git7399ad1
- Run 'make test' with libsolv build.

* Mon Apr 8 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-2.git7399ad1
- Rebase to upstream 7399ad1.
- Fixes RhBug:905209

* Mon Apr 8 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-1.gite372b78
- Rebase to upstream e372b78.
- Fixes RhBug:e372b78

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2.gitf663ca2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-17.git6c9d3eb
- Rebase to upstream 6c9d3eb.
- Drop the solv.i stdbool.h fix integrated upstream.
- Dropped the job reasons fix.

* Mon Jul 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-16.git1617994
- Fix build problems with Perl bindings.

* Mon Jul 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-15.git1617994
- Rebuilt after a failed mass rebuild.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-14.git1617994
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-13.git1617994%{?dist}
- preliminary fix for JOB resons in solver_describe_decision().

* Sun Jul 1 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-12.git1617994%{?dist}
- Rebase to upstream 1617994.
- Support for RPM_ADD_WITH_HDRID.

* Thu Jun  7 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-11.gitd39a42b%{?dist}
- Rebase to upstream d39a42b.
- Fix the epochs.
- Move the ruby modules into vendorarch dir, where they are expected.

* Thu May  17 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-9.git8cf7650%{?dist}
- Rebase to upstream 8cf7650.
- ruby bindings: fix USE_VENDORDIRS for Fedora.

* Thu Apr  12 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-7.gitaf1465a2%{?dist}
- Rebase to the upstream.
- Make repo_add_solv() work without stub repodata.

* Thu Apr  5 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-6.git80afaf7%{?dist}
- Rebuild for the new libdb package.

* Mon Apr  2 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-5.git80afaf7%{?dist}
- Rebuild for the new rpm package.

* Wed Mar 21 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-4.git80afaf7%{?dist}
- New upstream version, fix the .rpm release number.

* Wed Mar 21 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-3.git80afaf7%{?dist}
- New upstream version.

* Tue Feb  7 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-2.git857fe28%{?dist}
- Adapted to Ruby 1.9.3 (workaround for broken CMake in Fedora and
  ruby template correction in bindings)

* Thu Feb  2 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-1.git857fe28
- Initial packaging
- Based on Jindra Novy's spec file
- Based on upstream spec file
