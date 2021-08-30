# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore
%global wrappers gunicorn rq

Name:           python-%{pypi_name}
Version:        3.7.8
Release:        1%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Adjusts-worker-timeout-to-300-seconds.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-django >= 2.2.16
Conflicts:      python%{python3_pkgversion}-django >= 2.3
BuildRequires:  python%{python3_pkgversion}-pyyaml < 5.4.0
BuildRequires:  python%{python3_pkgversion}-pyyaml >= 5.1.1
BuildRequires:  python%{python3_pkgversion}-aiodns
BuildRequires:  python%{python3_pkgversion}-aiofiles
BuildRequires:  python%{python3_pkgversion}-aiohttp
BuildRequires:  python%{python3_pkgversion}-backoff
BuildRequires:  python%{python3_pkgversion}-click >= 7.0
BuildRequires:  python%{python3_pkgversion}-click < 8
BuildRequires:  python%{python3_pkgversion}-django
Requires:       python%{python3_pkgversion}-django-currentuser >= 0.5.1
Conflicts:      python%{python3_pkgversion}-django-currentuser >= 0.6
Requires:       python%{python3_pkgversion}-django-filter >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-filter >= 2.4
Requires:       python%{python3_pkgversion}-django-guardian >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-guardian >= 2.4
Requires:       python%{python3_pkgversion}-django-import-export >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-import-export >= 2.4
Requires:       python%{python3_pkgversion}-django-lifecycle >= 0.8.0
Conflicts:      python%{python3_pkgversion}-django-lifecycle >= 0.9
BuildRequires:  python%{python3_pkgversion}-django-prometheus
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.11.1
Conflicts:      python%{python3_pkgversion}-djangorestframework >= 3.12
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Conflicts:      python%{python3_pkgversion}-djangorestframework-queryfields >= 1.1
Requires:       python%{python3_pkgversion}-drf-access-policy >= 0.7.0
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 0.8
Requires:       python%{python3_pkgversion}-drf-nested-routers >= 0.91
Conflicts:      python%{python3_pkgversion}-drf-nested-routers >= 0.92
BuildRequires:  python%{python3_pkgversion}-drf-spectacular >= 0.9.13
BuildRequires:  python%{python3_pkgversion}-dynaconf
BuildRequires:  python%{python3_pkgversion}-dynaconf < 4.0
BuildRequires:  python%{python3_pkgversion}-dynaconf >= 3.0
Requires:       python%{python3_pkgversion}-gnupg >= 0.4.6
Conflicts:      python%{python3_pkgversion}-gnupg >= 0.5
BuildRequires:  python%{python3_pkgversion}-gunicorn < 20.1
BuildRequires:  python%{python3_pkgversion}-gunicorn >= 19.9
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-psycopg2 < 2.9
BuildRequires:  python%{python3_pkgversion}-psycopg2 >= 2.7
Requires:       python%{python3_pkgversion}-pygtrie >= 2.3.3
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.4
BuildRequires:  python%{python3_pkgversion}-redis >= 3.4.0
BuildRequires:  python%{python3_pkgversion}-rq < 1.6
BuildRequires:  python%{python3_pkgversion}-rq >= 1.1
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
Requires:       python%{python3_pkgversion}-django >= 2.2.16
Conflicts:      python%{python3_pkgversion}-django >= 2.3
Requires:       python%{python3_pkgversion}-pyyaml < 5.4.0
Requires:       python%{python3_pkgversion}-pyyaml >= 5.1.1
Requires:       python%{python3_pkgversion}-aiodns
Requires:       python%{python3_pkgversion}-aiofiles
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-backoff
Requires:       python%{python3_pkgversion}-click >= 7.0
Requires:       python%{python3_pkgversion}-click < 8
Requires:       python%{python3_pkgversion}-django
Requires:       python%{python3_pkgversion}-django-currentuser >= 0.5.1
Conflicts:      python%{python3_pkgversion}-django-currentuser >= 0.6
Requires:       python%{python3_pkgversion}-django-filter >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-filter >= 2.4
Requires:       python%{python3_pkgversion}-django-guardian >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-guardian >= 2.4
Requires:       python%{python3_pkgversion}-django-import-export >= 2.3.0
Conflicts:      python%{python3_pkgversion}-django-import-export >= 2.4
Requires:       python%{python3_pkgversion}-django-lifecycle >= 0.8.0
Conflicts:      python%{python3_pkgversion}-django-lifecycle >= 0.9
Requires:       python%{python3_pkgversion}-django-prometheus
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.11.1
Conflicts:      python%{python3_pkgversion}-djangorestframework >= 3.12
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Conflicts:      python%{python3_pkgversion}-djangorestframework-queryfields >= 1.1
Requires:       python%{python3_pkgversion}-drf-access-policy >= 0.7.0
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 0.8
Requires:       python%{python3_pkgversion}-drf-nested-routers >= 0.91
Conflicts:      python%{python3_pkgversion}-drf-nested-routers >= 0.92
Requires:       python%{python3_pkgversion}-drf-spectacular >= 0.9.13
Conflicts:      python%{python3_pkgversion}-drf-spectacular >= 0.9.14
Requires:       python%{python3_pkgversion}-dynaconf
Requires:       python%{python3_pkgversion}-dynaconf < 4.0
Requires:       python%{python3_pkgversion}-dynaconf >= 3.0
Requires:       python%{python3_pkgversion}-gnupg >= 0.4.6
Conflicts:      python%{python3_pkgversion}-gnupg >= 0.5
Requires:       python%{python3_pkgversion}-gunicorn < 20.1
Requires:       python%{python3_pkgversion}-gunicorn >= 19.9
Requires:       python%{python3_pkgversion}-jinja2
Requires:       python%{python3_pkgversion}-psycopg2 < 2.9
Requires:       python%{python3_pkgversion}-psycopg2 >= 2.7
Requires:       python%{python3_pkgversion}-pygtrie >= 2.3.3
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.4
Requires:       python%{python3_pkgversion}-redis >= 3.4.0
Requires:       python%{python3_pkgversion}-rq < 1.6
Requires:       python%{python3_pkgversion}-rq >= 1.1
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
%autosetup -p1 -n %{pypi_name}-%{version}
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
%{_libexecdir}/%{pypi_name}/*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 30 2021 Odilon Sousa <osousa@redhat.com> - 3.7.8-1
- Release python-pulpcore 3.7.8

* Sun May 09 2021 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.6-1
- Release python-pulpcore 3.7.6

* Wed Apr 14 2021 Evgeni Golov - 3.7.5-1
- Release python-pulpcore 3.7.5

* Tue Apr 06 2021 Evgeni Golov - 3.7.4-1
- Release python-pulpcore 3.7.4

* Wed Mar 03 2021 Brian Bouterse - 3.7.3-2
- Increase Pulp worker timeout to 300 seconds

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
