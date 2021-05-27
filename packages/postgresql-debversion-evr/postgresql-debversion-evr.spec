%if 0%{?rhel} <= 7
%global scl rh-postgresql12
%endif

%{?scl:%scl_package postgresql-debversion-evr}
%{!?scl:%global pkg_name %{name}}

Name:     %{?scl_prefix}postgresql-debversion-evr
Version:  0.0.1
Release:  1%{?dist}
Summary:  Debian version number compare function for PostgreSQL

Group:    Applications/System
License:  GPLv3
URL:      https://github.com/ATIX-AG/postgresql-debversion-evr
Source:   https://codeload.github.com/ATIX-AG/postgresql-debversion-evr/tar.gz/%{version}#/postgresql-debversion-evr-%{version}.tar.gz

Requires: %{?scl_prefix}postgresql-server
%{?scl:Requires: %{?scl_prefix}runtime}

%{?scl:BuildRequires: %{?scl_prefix}runtime}
BuildRequires: %{?scl_prefix}postgresql-devel

%if 0%{?rhel} > 7
BuildRequires: postgresql-server-devel
%endif

ExclusiveArch: x86_64

%description
Debian version numbers, used to version Debian binary and source
packages, have a defined format, including specifications for how
versions should be compared in order to sort them.  This package
implements a `deb_version_cmp` function for version comparison.

Version comparison uses the algorithm used by the Debian package
manager, dpkg, using the implementation from libapt-pkg.  This means
that value comparing uses the same logic as `dpkg --compare-versions`.

postgresql-debversion-evr implements the following features:

* The `deb_version_cmp` function (comparing two `text` values)

%prep
%autosetup -p1 -n postgresql-debversion-evr-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} - <<EOF}
%make_install
%{?scl:EOF}

%files
%{_datadir}/pgsql/extension/debversion_evr--%{version}.sql
%{_datadir}/pgsql/extension/debversion_evr.control
%doc README.md
%license LICENSE

%changelog
* Thu May 27 2021 Markus Bucher <bucher@atix.de> - 0.0.1-1
- new package
