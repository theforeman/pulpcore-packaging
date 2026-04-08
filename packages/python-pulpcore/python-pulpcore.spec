%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.85.15
Release:        3%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Mark-md5-usage-as-usedforsecurity-False.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 40.8.0
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.29.0
BuildRequires:  pyproject-rpm-macros


Requires:       python%{python3_pkgversion}-django >= 4.2.0
Conflicts:      python%{python3_pkgversion}-django == 5.0
Conflicts:      python%{python3_pkgversion}-django == 5.1
Requires:       python%{python3_pkgversion}-django < 5.3
Requires:       python%{python3_pkgversion}-aiodns >= 3.3.0
Requires:       python%{python3_pkgversion}-aiodns < 3.7
Requires:       python%{python3_pkgversion}-aiofiles >= 22.1
Requires:       python%{python3_pkgversion}-aiofiles < 24.2.0
Requires:       python%{python3_pkgversion}-aiohttp >= 3.8.3
Requires:       python%{python3_pkgversion}-aiohttp < 3.14
Requires:       python%{python3_pkgversion}-asyncio-throttle >= 1.0
Requires:       python%{python3_pkgversion}-asyncio-throttle < 1.0.3
Requires:       python%{python3_pkgversion}-backoff >= 2.1.2
Requires:       python%{python3_pkgversion}-backoff < 2.3
Requires:       python%{python3_pkgversion}-click >= 8.1.0
Requires:       python%{python3_pkgversion}-click < 8.3
Requires:       python%{python3_pkgversion}-cryptography >= 44.0.3
Requires:       python%{python3_pkgversion}-cryptography < 47.0
Requires:       python%{python3_pkgversion}-django-filter >= 23.1
Requires:       python%{python3_pkgversion}-django-filter <= 25.1
Requires:       python%{python3_pkgversion}-django-guid >= 3.3
Requires:       python%{python3_pkgversion}-django-guid < 3.6
Requires:       python%{python3_pkgversion}-django-import-export >= 2.9
Requires:       python%{python3_pkgversion}-django-import-export < 5.0
Requires:       python%{python3_pkgversion}-django-lifecycle >= 1.0.0
Requires:       python%{python3_pkgversion}-django-lifecycle <= 1.2.4
Requires:       python%{python3_pkgversion}-djangorestframework >= 3.14.0
Requires:       python%{python3_pkgversion}-djangorestframework <= 3.16.1
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0.0
Requires:       python%{python3_pkgversion}-djangorestframework-queryfields <= 1.1.0
Requires:       python%{python3_pkgversion}-drf-access-policy >= 1.1.2
Conflicts:      python%{python3_pkgversion}-drf-access-policy >= 1.5.1
Requires:       python%{python3_pkgversion}-drf-nested-routers >= 0.93.4
Requires:       python%{python3_pkgversion}-drf-nested-routers <= 0.94.2
Requires:       python%{python3_pkgversion}-drf-spectacular >= 0.27.2
Requires:       python%{python3_pkgversion}-drf-spectacular < 0.30
Requires:       python%{python3_pkgversion}-dynaconf >= 3.2.5
Requires:       python%{python3_pkgversion}-dynaconf <= 3.3.0
Requires:       python%{python3_pkgversion}-gnupg >= 0.5.0
Requires:       python%{python3_pkgversion}-gnupg <= 0.5.4
Requires:       python%{python3_pkgversion}-gunicorn >= 22.0
Requires:       python%{python3_pkgversion}-gunicorn < 23.1.0
Requires:       python%{python3_pkgversion}-jinja2 >= 3.1
Requires:       python%{python3_pkgversion}-jinja2 <= 3.1.6
Requires:       python%{python3_pkgversion}-importlib-metadata >= 6.0.1
Requires:       python%{python3_pkgversion}-importlib-metadata <= 6.0.1
Requires:       python%{python3_pkgversion}-json_stream >= 2.3.2
Requires:       python%{python3_pkgversion}-json_stream < 2.4
Requires:       python%{python3_pkgversion}-jq >= 1.6.0
Requires:       python%{python3_pkgversion}-jq < 1.11.0
Requires:       python%{python3_pkgversion}-pulp-glue >= 0.28.0
Requires:       python%{python3_pkgversion}-pulp-glue < 0.37
Requires:       python%{python3_pkgversion}-pyOpenSSL < 27.0
Requires:       python%{python3_pkgversion}-opentelemetry_api >= 1.27
Requires:       python%{python3_pkgversion}-opentelemetry_api < 1.37
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http >= 1.27
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http < 1.37
Requires:       python%{python3_pkgversion}-opentelemetry_sdk >= 1.27
Requires:       python%{python3_pkgversion}-opentelemetry_sdk < 1.37
Requires:       python%{python3_pkgversion}-protobuf >= 4.21.1
Requires:       python%{python3_pkgversion}-protobuf < 7.0
Requires:       python%{python3_pkgversion}-psycopg >= 3.1.8
Requires:       python%{python3_pkgversion}-psycopg < 3.3
Requires:       python%{python3_pkgversion}-psycopg_c >= 3.1.8
Requires:       python%{python3_pkgversion}-psycopg_c < 3.3
Requires:       python%{python3_pkgversion}-pygtrie >= 2.5
Conflicts:      python%{python3_pkgversion}-pygtrie >= 2.6
Requires:       python%{python3_pkgversion}-pyparsing >= 3.1.0
Requires:       python%{python3_pkgversion}-pyparsing < 3.3
Requires:       python%{python3_pkgversion}-pyyaml >= 5.1.1
Requires:       python%{python3_pkgversion}-pyyaml < 6.1
Requires:       python%{python3_pkgversion}-PyYAML < 6.1
Requires:       python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       python%{python3_pkgversion}-redis >= 4.3
Requires:       python%{python3_pkgversion}-redis < 6.5
Requires:       python%{python3_pkgversion}-tablib < 4.0
Conflicts:      python%{python3_pkgversion}-tablib == 3.6
Requires:       python%{python3_pkgversion}-url-normalize >= 1.4.3
Requires:       python%{python3_pkgversion}-url-normalize < 2.3
Requires:       python%{python3_pkgversion}-uuid6 >= 2023.5.2
Requires:       python%{python3_pkgversion}-uuid6 <= 2025.0.1
Requires:       python%{python3_pkgversion}-whitenoise >= 5.0.0
Requires:       python%{python3_pkgversion}-whitenoise < 6.10
Requires:       python%{python3_pkgversion}-yarl >= 1.9.1
Requires:       python%{python3_pkgversion}-yarl < 1.21

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

Provides:       %{pypi_name} = %{version}

Obsoletes:      python3.11-pulp-file < 1.16.0-1
Provides:       python%{python3_pkgversion}-pulp-file = %{version}
Provides:       pulpcore-plugin(file) = %{version}

Obsoletes:      python3.11-pulp-certguard < 1.8.0-1
Provides:       python%{python3_pkgversion}-pulp-certguard = %{version}
Provides:       pulpcore-plugin(certguard) = %{version}

# this is a soft-dependency in certguard, but for Katello we always want it
Requires:       python%{python3_pkgversion}-rhsm


%description
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
sed -i 's/psycopg\[binary\]/psycopg/' pyproject.toml

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/pulpcore-content
%{_bindir}/pulpcore-api
%{_bindir}/pulpcore-manager
%{_bindir}/pulpcore-worker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_file
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 08 2026 Odilon Sousa <osousa@redhat.com> - 3.85.15-3
- Relax jq constraint to < 1.11.0 (upstream pulpcore 3.85 allows < 1.11.0)

* Mon Apr 06 2026 Odilon Sousa <osousa@redhat.com> - 3.85.15-2
- Relax cryptography constraint to < 47.0 (upstream pyproject.toml allows < 47)

* Wed Mar 25 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.15-1
- Update to 3.85.15
- Relax PyOpenSSL constraint to < 27.0 (upstream raised ceiling in 3.85.15)

* Wed Mar 25 2026 Odilon Sousa <osousa@redhat.com> - 3.85.13-2
- Relax drf-spectacular constraint to allow 0.27.2 through 0.29.x

* Wed Mar 11 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.13-1
- Update to 3.85.13

* Mon Mar 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.12-1
- Update to 3.85.12

* Sat Jan 31 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.9-1
- Update to 3.85.9

* Wed Jan 28 2026 Odilon Sousa <osousa@redhat.com> - 3.85.7-2
- Update aiodns requirement

* Mon Jan 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.7-1
- Update to 3.85.7

* Thu Dec 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.4-1
- Update to 3.85.4

* Fri Nov 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.3-1
- Update to 3.85.3

* Tue Oct 28 2025 Odilon Sousa <osousa@redhat.com> - 3.85.1-2
- Allow newer version of PyYAML

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.1-1
- Update to 3.85.1

* Wed Sep 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.15-1
- Update to 3.73.15

* Mon Jul 14 2025 Evgeni Golov - 3.73.14-2
- drop libexec wrappers, nobody uses them anymore

* Mon Jun 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.14-1
- Update to 3.73.14

* Wed Jun 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.12-1
- Update to 3.73.12

* Thu Jun 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.11-1
- Update to 3.73.11

* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.9-1
- Update to 3.73.9

* Wed Apr 30 2025 Odilon Sousa <osousa@redhat.com> - 3.73.8-2
- Update requirement for pyparsing

* Fri Apr 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.8-1
- Update to 3.73.8

* Thu Apr 24 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.7-1
- Update to 3.73.7

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.6-1
- Update to 3.73.6

* Fri Apr 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.4-1
- Update to 3.73.4

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 3.73.3-2
- Add obsoletes for python3.11 package

* Fri Apr 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.3-1
- Update to 3.73.3

* Mon Mar 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.2-1
- Update to 3.73.2

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.11-1
- Update to 3.63.11

* Fri Feb 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.10-1
- Update to 3.63.10

* Fri Jan 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.9-1
- Update to 3.63.9

* Tue Jan 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.8-1
- Update to 3.63.8

* Thu Jan 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.7-1
- Update to 3.63.7

* Mon Dec 16 2024 Odilon Sousa <osousa@redhat.com> - 3.63.6-2
- Add a patch for FIPS compliency.

* Mon Dec 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.6-1
- Update to 3.63.6

* Thu Nov 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.4-1
- Update to 3.63.4

* Thu Nov 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.3-1
- Update to 3.63.3

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.2-1
- Update to 3.63.2

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.1-1
- Update to 3.63.1

* Wed Oct 09 2024 Odilon Sousa <osousa@redhat.com> - 3.63.0-3
- Add psycopg_c requirement

* Fri Oct 04 2024 Odilon Sousa <osousa@redhat.com> - 3.63.0-2
- Bump pulp-glue requirement

* Tue Oct 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.0-1
- Update to 3.63.0

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.20-1
- Update to 3.49.20

* Tue Sep 10 2024 Odilon Sousa <osousa@redhat.com> - 3.49.19-2
- Sync requirements with Pulp upstream requirements

* Tue Sep 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.19-1
- Update to 3.49.19

* Thu Aug 22 2024 Samir Jha <samirjha1525@gmail.com> - 3.49.17-2
- Apply patch to add indices to task table

* Mon Aug 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.17-1
- Update to 3.49.17

* Wed Aug 07 2024 Odilon Sousa <osousa@redhat.com> - 3.49.16-2
- Update requirement for python-cryptography

* Tue Aug 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.16-1
- Update to 3.49.16

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 3.49.15-1
- Release python-pulpcore 3.49.15

* Mon Jul 22 2024 Odilon Sousa <osousa@redhat.com> - 3.49.14-1
- Release python-pulpcore 3.49.14

* Mon May 27 2024 Odilon Sousa <osousa@redhat.com> - 3.49.10-1
- Release python-pulpcore 3.49.10

* Wed May 22 2024 Odilon Sousa <osousa@redhat.com> - 3.49.9-1
- Release python-pulpcore 3.49.9

* Wed May 22 2024 Odilon Sousa <osousa@redhat.com> - 3.49.8-2
- Relax pulp-glue requirements

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 3.49.8-1
- Release python-pulpcore 3.49.8

* Tue May 14 2024 Odilon Sousa <osousa@redhat.com> - 3.49.7-1
- Release python-pulpcore 3.49.7

* Wed May 08 2024 Odilon Sousa <osousa@redhat.com> - 3.49.6-1
- Update to 3.49.6

* Fri Apr 26 2024 Odilon Sousa <osousa@redhat.com> - 3.49.5-1
- Release python-pulpcore 3.49.5

* Thu Apr 18 2024 Evgeni Golov - 3.49.4-2
- Add rhsm dependency for certguard

* Tue Apr 16 2024 Evgeni Golov - 3.49.4-1
- Release python-pulpcore 3.49.4

* Mon Apr 15 2024 Patrick Creech <pcreech@redhat.com> - 3.49.3-2
- 'Provide' functionality for file and certguard plugins

* Wed Mar 27 2024 Odilon Sousa <osousa@redhat.com> - 3.49.3-1
- Release python-pulpcore 3.49.3

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
