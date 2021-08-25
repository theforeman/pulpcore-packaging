# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore
%global wrappers gunicorn rq pulpcore-worker

Name:           python-%{pypi_name}
Version:        3.14.5
Release:        2%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-django >= 2.2.24
Conflicts:      python%{python3_pkgversion}-django >= 2.3
BuildRequires:  python%{python3_pkgversion}-PyYAML < 5.5.0
BuildRequires:  python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       python%{python3_pkgversion}-aiodns >= 3.0.0
Conflicts:      python%{python3_pkgversion}-aiodns >= 3.1
BuildRequires:  python%{python3_pkgversion}-aiofiles >= 0.7.0
Requires:       python%{python3_pkgversion}-aiohttp >= 3.7.4
Conflicts:      python%{python3_pkgversion}-aiohttp >= 3.8
Requires:       python%{python3_pkgversion}-asyncio-throttle >= 1.0
Conflicts:      python%{python3_pkgversion}-asyncio-throttle >= 1.1
Requires:       python%{python3_pkgversion}-backoff >= 1.10.0
Conflicts:      python%{python3_pkgversion}-backoff >= 1.11
BuildRequires:  python%{python3_pkgversion}-click < 9.0
Requires:       python%{python3_pkgversion}-django-currentuser >= 0.5.3
Conflicts:      python%{python3_pkgversion}-django-currentuser >= 0.6
Requires:       python%{python3_pkgversion}-django-filter >= 2.4.0
Conflicts:      python%{python3_pkgversion}-django-filter >= 2.5
Requires:       python%{python3_pkgversion}-django-guardian >= 2.4.0
Conflicts:      python%{python3_pkgversion}-django-guardian >= 2.5
BuildRequires:  python%{python3_pkgversion}-django-guid < 3.0
Requires:       python%{python3_pkgversion}-django-import-export >= 2.5.0
Conflicts:      python%{python3_pkgversion}-django-import-export >= 2.6
Requires:       python%{python3_pkgversion}-django-lifecycle >= 0.9.1
Conflicts:      python%{python3_pkgversion}-django-lifecycle >= 0.10
BuildRequires:  python%{python3_pkgversion}-django-prometheus
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.12.4
Conflicts:      python%{python3_pkgversion}-djangorestframework >= 3.13
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Conflicts:      python%{python3_pkgversion}-djangorestframework-queryfields >= 1.1
Requires:       python%{python3_pkgversion}-drf-access-policy >= 0.9.0
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 0.10
BuildRequires:  python%{python3_pkgversion}-drf-nested-routers >= 0.93.3
BuildRequires:  python%{python3_pkgversion}-drf-spectacular >= 0.16.0
Requires:       python%{python3_pkgversion}-dynaconf >= 3.1.5
Conflicts:      python%{python3_pkgversion}-dynaconf >= 3.2
Requires:       python%{python3_pkgversion}-gnupg >= 0.4.7
Conflicts:      python%{python3_pkgversion}-gnupg >= 0.5
Requires:       python%{python3_pkgversion}-gunicorn >= 20.1.0
Conflicts:      python%{python3_pkgversion}-gunicorn >= 20.2
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-psycopg2 < 2.9
BuildRequires:  python%{python3_pkgversion}-psycopg2 >= 2.7
Requires:       python%{python3_pkgversion}-pygtrie >= 2.4.2
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.5
BuildRequires:  python%{python3_pkgversion}-redis >= 3.4.0
Requires:       python%{python3_pkgversion}-rq >= 1.8.1
Conflicts:      python%{python3_pkgversion}-rq >= 1.9
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools >= 39.2.0
BuildRequires:  python%{python3_pkgversion}-whitenoise < 5.3.0
BuildRequires:  python%{python3_pkgversion}-whitenoise >= 5.0.0

%description
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.2.24
Conflicts:      python%{python3_pkgversion}-django >= 2.3
Requires:       python%{python3_pkgversion}-PyYAML < 5.5.0
Requires:       python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       python%{python3_pkgversion}-aiodns >= 3.0.0
Conflicts:      python%{python3_pkgversion}-aiodns >= 3.1
Requires:       python%{python3_pkgversion}-aiofiles >= 0.7.0
Conflicts:      python%{python3_pkgversion}-aiofiles >= 0.7.1
Requires:       python%{python3_pkgversion}-aiohttp >= 3.7.4
Conflicts:      python%{python3_pkgversion}-aiohttp >= 3.8
Requires:       python%{python3_pkgversion}-aioredis >= 2.0.0
Conflicts:      python%{python3_pkgversion}-aioredis >= 2.1
Requires:       python%{python3_pkgversion}-asyncio-throttle >= 1.0
Conflicts:      python%{python3_pkgversion}-asyncio-throttle >= 1.1
Requires:       python%{python3_pkgversion}-backoff >= 1.10.0
Conflicts:      python%{python3_pkgversion}-backoff >= 1.11
Requires:       python%{python3_pkgversion}-click < 9.0
Requires:       python%{python3_pkgversion}-django-currentuser >= 0.5.3
Conflicts:      python%{python3_pkgversion}-django-currentuser >= 0.6
Requires:       python%{python3_pkgversion}-django-filter >= 2.4.0
Conflicts:      python%{python3_pkgversion}-django-filter >= 2.5
Requires:       python%{python3_pkgversion}-django-guardian >= 2.4.0
Conflicts:      python%{python3_pkgversion}-django-guardian >= 2.5
Requires:       python%{python3_pkgversion}-django-guid < 3.0
Requires:       python%{python3_pkgversion}-django-import-export >= 2.5.0
Conflicts:      python%{python3_pkgversion}-django-import-export >= 2.6
Requires:       python%{python3_pkgversion}-django-lifecycle >= 0.9.1
Conflicts:      python%{python3_pkgversion}-django-lifecycle >= 0.10
Requires:       python%{python3_pkgversion}-django-prometheus
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.12.4
Conflicts:      python%{python3_pkgversion}-djangorestframework >= 3.13
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Conflicts:      python%{python3_pkgversion}-djangorestframework-queryfields >= 1.1
Requires:       python%{python3_pkgversion}-drf-access-policy >= 0.9.0
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 0.10
Requires:       python%{python3_pkgversion}-drf-nested-routers >= 0.93.3
Conflicts:      python%{python3_pkgversion}-drf-nested-routers >= 0.93.4
Requires:       python%{python3_pkgversion}-drf-spectacular >= 0.17.3
Conflicts:      python%{python3_pkgversion}-drf-spectacular >= 0.18.0
Requires:       python%{python3_pkgversion}-dynaconf >= 3.1.5
Conflicts:      python%{python3_pkgversion}-dynaconf >= 3.2
Requires:       python%{python3_pkgversion}-gnupg >= 0.4.7
Conflicts:      python%{python3_pkgversion}-gnupg >= 0.5
Requires:       python%{python3_pkgversion}-gunicorn >= 20.1.0
Conflicts:      python%{python3_pkgversion}-gunicorn >= 20.2
Requires:       python%{python3_pkgversion}-jinja2
Requires:       python%{python3_pkgversion}-psycopg2 < 2.9
Requires:       python%{python3_pkgversion}-psycopg2 >= 2.7
Requires:       python%{python3_pkgversion}-pygtrie >= 2.4.2
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.5
Requires:       python%{python3_pkgversion}-redis >= 3.4.0
Requires:       python%{python3_pkgversion}-rq >= 1.8.1
Conflicts:      python%{python3_pkgversion}-rq >= 1.9
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-setuptools >= 39.2.0
Requires:       python%{python3_pkgversion}-whitenoise < 5.3.0
Requires:       python%{python3_pkgversion}-whitenoise >= 5.0.0

%description -n python%{python3_pkgversion}-%{pypi_name}
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

for wrapper in %{wrappers}
do
  printf '#!/bin/bash\nexec %s "$@"\n' ${wrapper} > ${wrapper}
done

%install
%py3_install

for wrapper in %{wrappers}
do
  install -D -m 755 ${wrapper} %{buildroot}%{_libexecdir}/%{pypi_name}/${wrapper}
done

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp-content
%{_bindir}/pulpcore-manager
%{_bindir}/pulpcore-worker
%{_libexecdir}/%{pypi_name}/*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.14.5-2
- Release python-pulpcore 3.14.5

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.14.5-1
- Release python-pulpcore 3.14.5

* Wed Aug 18 2021 Odilon Sousa <osousa@redhat.com> - 3.14.4-1
- Release python-pulpcore 3.14.4

* Mon Jul 26 2021 Justin Sherrill <jsherril@redhat.com> 3.14.3-1
- upgrade to 3.14.3

* Wed Jul 07 2021 Justin Sherrill <jsherril@redhat.com> 3.14.1-1
- update to 3.14.1

* Fri Jul 02 2021 Evgeni Golov - 3.14.0-1
- Release python-pulpcore 3.14.0

* Thu Jun 17 2021 Evgeni Golov - 3.13.0-2
- place the worker wrapper in libexec

* Fri Jun 11 2021 Evgeni Golov 3.13.0-1
- Update to 3.13.0

* Mon May 31 2021 Evgeni Golov - 3.11.2-1
- Release python-pulpcore 3.11.2

* Wed May 12 2021 Evgeni Golov 3.11.1-1
- Update to 3.11.1

* Wed Apr 28 2021 Justin Sherrill <jsherril@redhat.com> 3.11.0-2
- add patch for issue 8603

* Fri Mar 19 2021 Evgeni Golov 3.11.0-1
- Update to 3.11.0

* Wed Mar 03 2021 Brian Bouterse - 3.9.1-2
- Increase Pulp worker timeout to 300 seconds

* Fri Jan 22 2021 Evgeni Golov - 3.9.1-1
- Release python-pulpcore 3.9.1

* Mon Jan 11 2021 Evgeni Golov - 3.9.0-1
- Update to 3.9.0

* Mon Dec 21 2020 Evgeni Golov - 3.8.1-2
- Drop django-storages requirement, it was an oversight to add it

* Fri Dec 11 2020 Evgeni Golov 3.8.1-1
- Update to 3.8.1

* Tue Nov 03 2020 Evgeni Golov 3.7.3-1
- Update to 3.7.3

* Fri Oct 23 2020 Evgeni Golov - 3.7.2-1
- Release python-pulpcore 3.7.2

* Fri Oct 09 2020 Evgeni Golov - 3.7.1-3
- Bump dynaconf Requires to skip RCs

* Wed Oct 07 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.1-2
- Add libexec wrappers for gunicorn and rq

* Wed Sep 30 2020 Evgeni Golov 3.7.1-1
- Update to 3.7.1

* Mon Sep 07 2020 Evgeni Golov 3.6.3-1
- Update to 3.6.3

* Thu Sep 03 2020 Justin Sherrill <jsherril@redhat.com> 3.6.2-2
- add missing jinja2 dep

* Thu Sep 03 2020 Evgeni Golov 3.6.2-1
- Update to 3.6.2

* Tue Aug 25 2020 Evgeni Golov 3.6.0-1
- Update to 3.6.0

* Thu Jun 04 2020 Evgeni Golov 3.4.1-1
- Update to 3.4.1

* Fri May 08 2020 Evgeni Golov 3.3.1-1
- Update to 3.3.1

* Tue Apr 28 2020 Evgeni Golov 3.3.0-1
- Update to 3.3.0

* Wed Mar 18 2020 Samir Jha 3.2.1-1
- Update to 3.2.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.1-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 3.0.1-1
- Update to 3.0.1

* Fri Dec 13 2019 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Mon Nov 18 2019 Evgeni Golov - 3.0.0rc8-1
- Initial package.
