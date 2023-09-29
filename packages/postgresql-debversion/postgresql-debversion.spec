%global debug_package %{nil}
Name:     postgresql-debversion
Version:  1.1.1
Release:  4%{?dist}
Summary:  Debian version number type for PostgreSQL

Group:    Applications/System
License:  GPLv3
URL:      https://salsa.debian.org/postgresql/postgresql-debversion
Source0:  https://salsa.debian.org/postgresql/postgresql-debversion/-/archive/v%{version}/postgresql-debversion-v%{version}.tar.gz
Patch0:   0001-Copy-relevant-code-from-apt-pkg-to-ease-packaging.patch
Patch1:   0002-set_superuser.patch

Requires: postgresql-server

BuildRequires: postgresql-server-devel
BuildRequires: gcc-c++
%if 0%{?rhel} == 8
BuildRequires: libpq-devel
%endif

ExclusiveArch: x86_64

%description
Debian version numbers, used to version Debian binary and source
packages, have a defined format, including specifications for how
versions should be compared in order to sort them.  This package
implements a `debversion` type to represent Debian version numbers
within the PostgreSQL database.  This also includes operators for
version comparison and index operator classes for creating indexes on
the debversion type.

Version comparison uses the algorithm used by the Debian package
manager, dpkg, using the implementation from libapt-pkg.  This means
that columns in tables using the debversion type may be sorted and
compared correctly using the same logic as `dpkg --compare-versions`.
It is also possible to create indexes on these columns.

postgresql-debversion implements the following features:

* The `debversion` type (internally derived from the `text` type)
* A full set of operators for version comparison (< <= = <> >= >)
  including commutator and negator optimisation hints
* Operator classes for btree and hash indexes
* The aggregate functions `min()` and `max()`

%prep
%autosetup -p1 -n postgresql-debversion-v%{version}

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%make_install

%files
%{_libdir}/pgsql/debversion.so
%{_datadir}/pgsql/extension/debversion--1.0.5--1.0.6.sql
%{_datadir}/pgsql/extension/debversion--1.0.6--1.0.7.sql
%{_datadir}/pgsql/extension/debversion--1.0.7--1.0.8.sql
%{_datadir}/pgsql/extension/debversion--1.0.8--1.1.sql
%{_datadir}/pgsql/extension/debversion--1.1.sql
%{_datadir}/pgsql/extension/debversion--unpackaged--1.0.5.sql
%{_datadir}/pgsql/extension/debversion.control
%doc README.md
%license COPYING

%changelog
* Fri Sep 29 2023 Odilon Sousa <osousa@redhat.com> - 1.1.1-4
- Disable debug_package

* Tue Sep 26 2023 Odilon Sousa <osousa@redhat.com> - 1.1.1-3
- Remove SCL Macros

* Tue Jun 09 2020 Justin Sherrill <jsherril@redhat.com> 1.1.1-2
- add patch to allow nonsuperuser access

* Fri Jan 03 2020 Matthias Dellweg <dellweg@atix.de> - 1.1.1-1
- new package
