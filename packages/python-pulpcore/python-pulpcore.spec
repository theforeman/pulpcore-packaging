%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_libexecdir:%global _root_libexecdir %{_libexecdir}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore
%global wrappers gunicorn pulpcore-worker
%global scl_wrappers pulp-content pulpcore-manager

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.28.16
Release:        1%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools < 66.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 39.2.0

%description
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django >= 4.2.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-django >= 4.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML < 6.1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiodns >= 3.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-aiodns >= 3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiofiles >= 22.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.8.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aioredis >= 2.0.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-aioredis >= 2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle >= 1.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle >= 1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-backoff >= 2.1.2
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-backoff >= 2.2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click >= 8.1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click <= 8.1.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-filter >= 23.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-django-filter >= 23.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-guid >= 3.3
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-django-guid >= 3.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-import-export >= 2.9
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-django-import-export >= 3.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle >= 1.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle >= 1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.14.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.14.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields >= 1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy >= 1.1.2
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy >= 1.5.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-nested-routers = 0.93.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-spectacular = 0.26.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dynaconf >= 3.1.12
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-dynaconf >= 3.1.13
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gnupg >= 0.5.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-gnupg >= 0.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gunicorn >= 20.1.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-gunicorn >= 20.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jinja2 >= 3.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-jinja2 >= 3.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-naya >= 1.1.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-naya >= 1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 6.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata <= 6.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-glue >= 0.18.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-glue < 0.22
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_distro_otlp >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_distro_otlp <= 0.40b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http >= 1.17.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http <= 1.19.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_instrumentation_django >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_instrumentation_django <= 0.40b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_instrumentation_wsgi >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry_instrumentation_wsgi <= 0.40b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf >= 4.21.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf < 4.23.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg >= 2.9.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg <= 3.1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygtrie >= 2.5
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-pygtrie >= 2.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-redis >= 4.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-redis < 4.5.6
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 67.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 39.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-url-normalize >= 1.4.3
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-url-normalize >= 1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uuid6 >= 2023.5.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uuid6 <= 2024.1.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-whitenoise >= 6.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-whitenoise >= 5.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-yarl >= 1.8
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-yarl >= 1.9.3

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

Provides:       %{pypi_name} = %{version}

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Pulp is a platform for managing repositories of content, such as software
packages, and pushing that content out to large numbers of consumers.

Using Pulp you can:
- Locally mirror all or part of a repository
- Host your own content in a new repository
- Manage content from multiple sources in one place
- Promote content through different repos in an organized way


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# relax cryptography requirement
# see https://pulp.plan.io/issues/9367
sed -i '/cryptography/ s/~=.*//' requirements.txt

# relax otel requirement
sed -i "/opentelemetry/ s/39b0/40b0/" requirements.txt
sed -i "/opentelemetry-exporter-otlp-proto-http/ s/1.18.0/1.19.0/" requirements.txt

# psycopg 'binary' extra isn't needed in production
sed -i 's/psycopg\[binary\]/psycopg/' requirements.txt

%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}
for wrapper in %{wrappers}
do
  printf '#!/bin/bash\n%{?scl:source scl_source enable tfm-pulpcore \n}exec %s "$@"\n' ${wrapper} > ${wrapper}
done
%if 0%{?scl:1}
for wrapper in %{scl_wrappers}
do
  printf '#!/bin/bash\n%{?scl:source scl_source enable tfm-pulpcore \n}exec %s "$@"\n' ${wrapper} > ${wrapper}
done
%endif


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}
for wrapper in %{wrappers}
do
  install -D -m 755 ${wrapper} %{buildroot}%{_root_libexecdir}/%{pypi_name}/${wrapper}
done
%if 0%{?scl:1}
for wrapper in %{scl_wrappers}
do
  install -D -m 755 ${wrapper} %{buildroot}%{_root_bindir}/${wrapper}
done
%endif
%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%if 0%{?scl:1}
%{_root_bindir}/pulp-content
%{_root_bindir}/pulpcore-manager
%endif
%{_bindir}/pulp-content
%{_bindir}/pulpcore-manager
%{_bindir}/pulpcore-worker
%{_root_libexecdir}/%{pypi_name}/*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
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
