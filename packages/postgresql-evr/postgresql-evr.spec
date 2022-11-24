Name:		postgresql-evr
Version:	0.0.2
Release:	2%{?dist}
Summary:	RPM evr extension for PostgreSQL

License:	GPLv3

BuildArch: noarch
BuildRequires: postgresql-server-devel
Requires: postgresql-server

URL: https://github.com/Katello/postgresql-evr
Source0: https://codeload.github.com/Katello/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz

%description
Installs files required to create evr extension in PostgreSQL.

%prep
%autosetup -p1 -n %{name}-%{version}

%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files

%{_datadir}/pgsql/extension/evr.control
%{_datadir}/pgsql/extension/evr--%{version}.sql


%changelog
* Thu Nov 24 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.2-2
- Remove SCL macros
- Declare as noarch

* Mon Apr 13 2020 ianballou <ianballou67@gmail.com> 0.0.2-1
- remove superuser requirement

* Mon Mar 09 2020 Justin Sherrill <jsherril@redhat.com> 0.0.1-2
- do not build a debug package on el8

* Mon Mar 02 2020 Ian Ballou <ianballou67@gmail.com> - 0.0.1-1
- postgresql-evr initial creation
