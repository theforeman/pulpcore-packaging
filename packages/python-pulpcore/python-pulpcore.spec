%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_libexecdir:%global _root_libexecdir %{_libexecdir}}
%{?python_disable_dependency_generator}
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore
%global wrappers gunicorn pulpcore-worker pulp-content pulpcore-manager

Name:           python-%{pypi_name}
Version:        3.49.1
Release:        2%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools < 66.0.0
BuildRequires:  python%{python3_pkgversion}-setuptools >= 39.2.0

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
Requires:       python%{python3_pkgversion}-django >= 4.2.0
Conflicts:      python%{python3_pkgversion}-django >= 4.3.0
Requires:       python%{python3_pkgversion}-PyYAML < 6.1.0
Requires:       python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       python%{python3_pkgversion}-aiodns >= 3.0.0
Conflicts:      python%{python3_pkgversion}-aiodns >= 3.1.2
Requires:       python%{python3_pkgversion}-aiofiles >= 22.1
Requires:       python%{python3_pkgversion}-aiofiles < 23.3.0
Requires:       python%{python3_pkgversion}-aiohttp >= 3.8.1
Conflicts:      python%{python3_pkgversion}-aiohttp >= 3.9.5
Requires:       python%{python3_pkgversion}-aioredis >= 2.0.1
Conflicts:      python%{python3_pkgversion}-aioredis >= 2.1
Requires:       python%{python3_pkgversion}-asyncio-throttle >= 1.0
Conflicts:      python%{python3_pkgversion}-asyncio-throttle >= 1.1
Requires:       python%{python3_pkgversion}-backoff >= 2.1.2
Conflicts:      python%{python3_pkgversion}-backoff >= 2.2.2
Requires:       python%{python3_pkgversion}-click >= 8.1.0
Requires:       python%{python3_pkgversion}-click < 8.1.8
Requires:       python%{python3_pkgversion}-cryptography >= 38.0.1
Requires:       python%{python3_pkgversion}-cryptography < 42.0.6
Requires:       python%{python3_pkgversion}-django-filter >= 23.1
Requires:       python%{python3_pkgversion}-django-filter <= 23.5
Requires:       python%{python3_pkgversion}-django-guid >= 3.3
Requires:       python%{python3_pkgversion}-django-guid <= 3.4.0
Requires:       python%{python3_pkgversion}-django-import-export >= 2.9
Requires:       python%{python3_pkgversion}-django-import-export < 3.4.0
Requires:       python%{python3_pkgversion}-django-lifecycle >= 1.0.0
Requires:       python%{python3_pkgversion}-django-lifecycle <= 1.1.2
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.14.0
Conflicts:      python%{python3_pkgversion}-djangorestframework >= 3.14.1
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields <= 1.1.0
Requires:       python%{python3_pkgversion}-drf-access-policy >= 1.1.2
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 1.5.1
Requires:       python%{python3_pkgversion}-drf-nested-routers >= 0.93.4
Requires:       python%{python3_pkgversion}-drf-nested-routers <= 0.93.5
Requires:       python%{python3_pkgversion}-drf-spectacular = 0.26.5
Requires:       python%{python3_pkgversion}-dynaconf >= 3.1.12
Requires:       python%{python3_pkgversion}-dynaconf <= 3.2.5
Requires:       python%{python3_pkgversion}-gnupg >= 0.5.0
Requires:       python%{python3_pkgversion}-gnupg <= 0.5.2
Requires:       python%{python3_pkgversion}-gunicorn >= 20.1.0
Requires:       python%{python3_pkgversion}-gunicorn <= 21.2.0
Requires:       python%{python3_pkgversion}-jinja2 >= 3.1
Requires:       python%{python3_pkgversion}-jinja2 <= 3.1.3
Requires:       python%{python3_pkgversion}-importlib-metadata >= 6.0.1
Requires:       python%{python3_pkgversion}-importlib-metadata <= 6.0.1
Requires:       python%{python3_pkgversion}-json_stream >= 2.3.2
Requires:       python%{python3_pkgversion}-json_stream < 2.4
Requires:       python%{python3_pkgversion}-jq >= 1.6.0
Requires:       python%{python3_pkgversion}-jq < 1.7.0
Requires:       python%{python3_pkgversion}-pulp-glue >= 0.18.0
Requires:       python%{python3_pkgversion}-pulp-glue < 0.24
Requires:       python%{python3_pkgversion}-pyOpenSSL < 25
Requires:       python%{python3_pkgversion}-opentelemetry_distro_otlp >= 0.38b0
Requires:       python%{python3_pkgversion}-opentelemetry_distro_otlp <= 0.44b0
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http >= 1.17.0
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http <= 1.23.0
Requires:       python%{python3_pkgversion}-opentelemetry_instrumentation_django >= 0.38b0
Requires:       python%{python3_pkgversion}-opentelemetry_instrumentation_django <= 0.44b0
Requires:       python%{python3_pkgversion}-opentelemetry_instrumentation_wsgi >= 0.38b0
Requires:       python%{python3_pkgversion}-opentelemetry_instrumentation_wsgi <= 0.44b0
Requires:       python%{python3_pkgversion}-protobuf >= 4.21.1
Requires:       python%{python3_pkgversion}-protobuf < 4.25.4
Requires:       python%{python3_pkgversion}-psycopg >= 3.1.8
Requires:       python%{python3_pkgversion}-psycopg <= 3.1.18
Requires:       python%{python3_pkgversion}-pygtrie >= 2.5
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.6
Requires:       python%{python3_pkgversion}-pyparsing >= 3.1.0 
Requires:       python%{python3_pkgversion}-pyparsing <= 3.1.1
Requires:       python%{python3_pkgversion}-pyyaml >= 5.1.1
Requires:       python%{python3_pkgversion}-pyyaml <= 6.0.1
Requires:       python%{python3_pkgversion}-redis >= 4.3
Requires:       python%{python3_pkgversion}-redis < 5.0.3
Requires:       python%{python3_pkgversion}-setuptools >= 39.2.0
Requires:       python%{python3_pkgversion}-setuptools < 69.2.0
Requires:       python%{python3_pkgversion}-url-normalize >= 1.4.3
Conflicts:      python%{python3_pkgversion}-url-normalize >= 1.5
Requires:       python%{python3_pkgversion}-uuid6 >= 2023.5.2
Requires:       python%{python3_pkgversion}-uuid6 <= 2024.1.12
Conflicts:      python%{python3_pkgversion}-whitenoise >= 6.5.0
Requires:       python%{python3_pkgversion}-whitenoise >= 5.0.0
Requires:       python%{python3_pkgversion}-yarl >= 1.8
Requires:       python%{python3_pkgversion}-yarl < 1.9.5

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif
# Pulp-file and Pulp-certguard are now part of pulpcore
Obsoletes:      python3.11-pulp-file < 1.16.0-1
Obsoletes:      python3.11-pulp-certguard < 1.8.0-1

Provides:       %{pypi_name} = %{version}

%description -n python%{python3_pkgversion}-%{pypi_name}
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# psycopg 'binary' extra isn't needed in production
sed -i 's/psycopg\[binary\]/psycopg/' requirements.txt



%build
set -ex
%py3_build
for wrapper in %{wrappers}
do
  printf '#!/bin/bash\nexec %s "$@"\n' ${wrapper} > ${wrapper}
done


%install
set -ex
%py3_install
for wrapper in %{wrappers}
do
  install -D -m 755 ${wrapper} %{buildroot}%{_root_libexecdir}/%{pypi_name}/${wrapper}
done

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulpcore-content
%{_bindir}/pulpcore-api
%{_bindir}/pulpcore-manager
%{_bindir}/pulpcore-worker
%{_root_libexecdir}/%{pypi_name}/*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_file
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Mar 27 2024 Odilon Sousa <osousa@redhat.com> - 3.49.1-2
- Obsolete pulp-file and pulp-certguard

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.49.1-1
- Release python-pulpcore 3.49.1

* Tue Mar 05 2024 Odilon Sousa <osousa@redhat.com> - 3.39.11-1
- Release python-pulpcore 3.39.11

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 3.39.8-1
- Release python-pulpcore 3.39.8

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 3.39.4-3
- Fix wrappers on pulpcore package after scl removal

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> 3.39.4-2
- Remove SCL bits

* Wed Jan 03 2024 Odilon Sousa <osousa@redhat.com> - 3.39.4-1
- Release python-pulpcore 3.39.4

* Mon Dec 11 2023 Ian Ballou <ianballou67@gmail.com> - 3.39.3-1
- Update to 3.39.3

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.39.2-2
- Obsolete python39 packages for a smooth upgrade

* Wed Nov 08 2023 Odilon Sousa <osousa@redhat.com> - 3.39.2-1
- Release python-pulpcore 3.39.2

* Mon Nov 06 2023 Odilon Sousa <osousa@redhat.com> - 3.28.19-1
- Release python-pulpcore 3.28.19

* Wed Oct 18 2023 Odilon Sousa <osousa@redhat.com> - 3.28.18-1
- Release python-pulpcore 3.28.18

* Mon Oct 02 2023 Odilon Sousa <osousa@redhat.com> - 3.28.16-1
- Release python-pulpcore 3.28.16

* Wed Sep 20 2023 Odilon Sousa <osousa@redhat.com> - 3.28.15-1
- Release python-pulpcore 3.28.15

* Thu Aug 10 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-7
- Add opentelemetry_distro_otlp meta package requirement

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-6
- Remove psycopg binary extra, isn't needed in pulpcore

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-5
- Relax opentelemetry requirements

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-4
- Adjust python-uuid6 requirements

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-3
- Change django-filter requirement

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-2
- Remove python-django-currentuser dependency

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-1
- Release python-pulpcore 3.28.10

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 3.28.5-1
- Release python-pulpcore 3.28.5

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-4
- Fix django-import-export requirement for Pulpcore 3.22

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-3
- Update python-backoff requirement for Pulpcore package

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-2
- Bump pulpcore release to fix one dependency requirement

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-1
- Release python-pulpcore 3.22.2

* Fri Feb 03 2023 Odilon Sousa <osousa@redhat.com> - 3.21.5-1
- Release python-pulpcore 3.21.5

* Mon Jan 23 2023 Patrick Creech <pcreech@redhat.com> - 3.21.4-1
- Release python-pulpcore 3.21.4

* Tue Sep 20 2022 Odilon Sousa 3.21.0-1
- Update to 3.21.0

* Wed Sep 14 2022 Odilon Sousa <osousa@redhat.com> - 3.18.10-1
- Release python-pulpcore 3.18.10

* Wed Aug 03 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.18.6-1
- Release python-pulpcore 3.18.6

* Thu May 26 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-2
- Adding a sed to change redis on requirements.txt, from ~= to >=

* Wed May 25 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-1
- Release python-pulpcore 3.18.5

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.18.4-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 29 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-3
- Fixing pulpcore requirements for djangorestframework

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-2
- Fixing the requirement for url-normalize

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-1
- Release python-pulpcore 3.18.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.3-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.17.3-1
- Release python-pulpcore 3.17.3

* Thu Dec 02 2021 Justin Sherrill <jsherril@redhat.com> 3.16.1-1
- update to 3.16.1

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 3.16.0-2
- Solving conflict with django-filter

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 3.16.0-1
- Release python-pulpcore 3.16.0

* Tue Oct 26 2021 Evgeni Golov - 3.15.2-4
- Also obsolete python3-pulpcore on EL7

* Wed Oct 20 2021 Evgeni Golov - 3.15.2-3
- Add provides for 'pulpcore'

* Wed Sep 29 2021 Evgeni Golov - 3.15.2-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 3.15.2-1
- Update to 3.15.2

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
