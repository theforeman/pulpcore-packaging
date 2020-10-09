# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore
%global wrappers gunicorn rq

Name:           python-%{pypi_name}
Version:        3.7.1
Release:        3%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-django >= 2.2.16
Conflicts:      python3-django >= 2.3
BuildRequires:  python3-pyyaml < 5.4.0
BuildRequires:  python3-pyyaml >= 5.1.1
BuildRequires:  python3-aiodns
BuildRequires:  python3-aiofiles
BuildRequires:  python3-aiohttp
BuildRequires:  python3-backoff
BuildRequires:  python3-django
Requires:       python3-django-cleanup >= 5.1.0
Conflicts:      python3-django-cleanup >= 5.2
Requires:       python3-django-currentuser >= 0.5.1
Conflicts:      python3-django-currentuser >= 0.6
Requires:       python3-django-filter >= 2.3.0
Conflicts:      python3-django-filter >= 2.4
Requires:       python3-django-guardian >= 2.3.0
Conflicts:      python3-django-guardian >= 2.4
Requires:       python3-django-import-export >= 2.3.0
Conflicts:      python3-django-import-export >= 2.4
Requires:       python3-django-lifecycle >= 0.7.7
Conflicts:      python3-django-lifecycle >= 0.8
Requires:       python3-djangorestframework >= 3.11.1
Conflicts:      python3-djangorestframework >= 3.12
Requires:       python3-djangorestframework-queryfields >= 1.0.0
Conflicts:      python3-djangorestframework-queryfields >= 1.1
Requires:       python3-drf-access-policy >= 0.7.0
Conflicts:      python3-drf-access-policy >= 0.8
Requires:       python3-drf-nested-routers >= 0.91
Conflicts:      python3-drf-nested-routers >= 0.92
BuildRequires:  python3-dynaconf
BuildRequires:  python3-dynaconf < 4.0
BuildRequires:  python3-dynaconf >= 3.0
Requires:       python3-gnupg >= 0.4.6
Conflicts:      python3-gnupg >= 0.5
BuildRequires:  python3-gunicorn < 20.1
BuildRequires:  python3-gunicorn >= 19.9
BuildRequires:  python3-jinja2
BuildRequires:  python3-psycopg2 < 2.9
BuildRequires:  python3-psycopg2 >= 2.7
Requires:       python3-pygtrie >= 2.3.3
Conflicts:      python3-pygtrie >= 2.4
BuildRequires:  python3-redis >= 3.4.0
BuildRequires:  python3-rq < 1.6
BuildRequires:  python3-rq >= 1.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools >= 39.2.0
BuildRequires:  python3-whitenoise < 5.3.0
BuildRequires:  python3-whitenoise >= 5.0.0

%description
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.2.16
Conflicts:      python3-django >= 2.3
Requires:       python3-pyyaml < 5.4.0
Requires:       python3-pyyaml >= 5.1.1
Requires:       python3-aiodns
Requires:       python3-aiofiles
Requires:       python3-aiohttp
Requires:       python3-backoff
Requires:       python3-django
Requires:       python3-django-cleanup >= 5.1.0
Conflicts:      python3-django-cleanup >= 5.2
Requires:       python3-django-currentuser >= 0.5.1
Conflicts:      python3-django-currentuser >= 0.6
Requires:       python3-django-filter >= 2.3.0
Conflicts:      python3-django-filter >= 2.4
Requires:       python3-django-guardian >= 2.3.0
Conflicts:      python3-django-guardian >= 2.4
Requires:       python3-django-import-export >= 2.3.0
Conflicts:      python3-django-import-export >= 2.4
Requires:       python3-django-lifecycle >= 0.7.7
Conflicts:      python3-django-lifecycle >= 0.8
Requires:       python3-djangorestframework >= 3.11.1
Conflicts:      python3-djangorestframework >= 3.12
Requires:       python3-djangorestframework-queryfields >= 1.0.0
Conflicts:      python3-djangorestframework-queryfields >= 1.1
Requires:       python3-drf-access-policy >= 0.7.0
Conflicts:      python3-drf-access-policy >= 0.8
Requires:       python3-drf-nested-routers >= 0.91
Conflicts:      python3-drf-nested-routers >= 0.92
Requires:       python3-drf-spectacular >= 0.9.13
Conflicts:      python3-drf-spectacular >= 0.9.14
Requires:       python3-dynaconf
Requires:       python3-dynaconf < 4.0
Requires:       python3-dynaconf >= 3.0.0-1
Requires:       python3-gnupg >= 0.4.6
Conflicts:      python3-gnupg >= 0.5
Requires:       python3-gunicorn < 20.1
Requires:       python3-gunicorn >= 19.9
Requires:       python3-jinja2
Requires:       python3-psycopg2 < 2.9
Requires:       python3-psycopg2 >= 2.7
Requires:       python3-pygtrie >= 2.3.3
Conflicts:      python3-pygtrie >= 2.4
Requires:       python3-redis >= 3.4.0
Requires:       python3-rq < 1.6
Requires:       python3-rq >= 1.1
Requires:       python3-setuptools
Requires:       python3-setuptools >= 39.2.0
Requires:       python3-whitenoise < 5.3.0
Requires:       python3-whitenoise >= 5.0.0

%description -n python3-%{pypi_name}
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp-content
%{_bindir}/pulpcore-manager
%{_libexecdir}/%{pypi_name}/*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
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
