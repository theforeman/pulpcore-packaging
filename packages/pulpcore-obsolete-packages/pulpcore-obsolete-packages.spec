Name: pulpcore-obsolete-packages
Version: 1.5.0
Release: 2%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/pulpcore-packaging
BuildArch: noarch

Obsoletes:      python3-django-currentuser < 0.5.3-6
Obsoletes:      python3.11-pymongo < 3.11.0-8
Obsoletes:      python3.11-mongoengine < 0.20.0-8
%if 0%{?rhel} == 8
Obsoletes:      python3-pulp-2to3-migration < 0.12.0-3
Obsoletes:      python39-django-currentuser < 0.5.3-6
Obsoletes:      python39-importlib-resources < 5.4.0-6
Obsoletes:      python39-django-guardian < 2.4.0-7
Obsoletes:      python39-aiodns < 3.0.0-4
Obsoletes:      python39-aiohttp < 4.0.0-1
Obsoletes:      python39-aiohttp-xmlrpc < 1.5.0-3
Obsoletes:      python39-pexpect < 4.8.0-3
Obsoletes:      python39-requests < 2.31.0-2
Obsoletes:      python39-wcmatch < 8.3-3
Obsoletes:      python39-aiohttp-socks < 0.7.1-4
Obsoletes:      python39-pypi-simple < 0.9.0-3
%endif

### OpenTelemetry unneeded packages

Obsoletes:      python3.11-opentelemetry_distro < 0.51b0-1
Obsoletes:      python3.11-opentelemetry_distro_otlp < 0.51b0-1
Obsoletes:      python3.11-opentelemetry_exporter_otlp < 1.30.0-1
Obsoletes:      python3.11-opentelemetry_exporter_otlp_proto_grpc < 1.30.0-1
Obsoletes:      python3.11-opentelemetry_instrumentation < 0.51b0-1
Obsoletes:      python3.11-opentelemetry_instrumentation_django < 0.51b0-1
Obsoletes:      python3.11-opentelemetry_instrumentation_wsgi < 0.51b0-1
Obsoletes:      python3.11-opentelemetry_util_http < 0.51b0-1

## Python 3.11 to 3.12 transition
### Do not obsolete RHEL-owned packages: python3.11-libs, python3.11-pip-wheel,
### python3.11-setuptools, python3.11-setuptools-wheel

Obsoletes:      python3.11-aiodns < 3.2.0-2
Obsoletes:      python3.11-aiofiles < 24.1.0-2
Obsoletes:      python3.11-aiohappyeyeballs < 2.4.4-2
Obsoletes:      python3.11-aiohttp < 3.10.11-2
Obsoletes:      python3.11-aiohttp-xmlrpc < 1.5.0-7
Obsoletes:      python3.11-aioredis < 2.0.1-8
Obsoletes:      python3.11-aiosignal < 1.3.2-2
Obsoletes:      python3.11-asgiref < 3.8.1-2
Obsoletes:      python3.11-async-lru < 2.0.4-2
Obsoletes:      python3.11-async-timeout < 4.0.3-2
Obsoletes:      python3.11-asyncio-throttle < 1.0.2-8
Obsoletes:      python3.11-attrs < 22.2.0-2
Obsoletes:      python3.11-backoff < 2.2.1-6
Obsoletes:      python3.11-bleach < 3.3.1-7
Obsoletes:      python3.11-bleach-allowlist < 1.0.3-8
Obsoletes:      python3.11-bracex < 2.5-2
Obsoletes:      python3.11-brotli < 1.2.0-2
Obsoletes:      python3.11-certifi < 2024.12.14-2
Obsoletes:      python3.11-cffi < 1.17.1-2
Obsoletes:      python3.11-charset-normalizer < 3.4.1-2
Obsoletes:      python3.11-click < 8.1.7-2
Obsoletes:      python3.11-click-shell < 2.1-8
Obsoletes:      python3.11-colorama < 0.4.4-8
Obsoletes:      python3.11-commonmark < 0.9.1-10
Obsoletes:      python3.11-contextlib2 < 21.6.0-8
Obsoletes:      python3.11-cryptography < 45.0.3-0.2
Obsoletes:      python3.11-dataclasses < 0.8-8
Obsoletes:      python3.11-dateutil < 2.8.2-8
Obsoletes:      python3.11-defusedxml < 0.7.1-8
Obsoletes:      python3.11-deprecated < 1.2.18-2
Obsoletes:      python3.11-diff-match-patch < 20241021-2
Obsoletes:      python3.11-docutils < 0.20.1-5
Obsoletes:      python3.11-ecdsa < 0.18.0-6
Obsoletes:      python3.11-et-xmlfile < 1.1.0-7
Obsoletes:      python3.11-frozenlist < 1.5.0-2
Obsoletes:      python3.11-future < 0.18.3-6
Obsoletes:      python3.11-gitdb < 4.0.12-2
Obsoletes:      python3.11-gitpython < 3.1.44-2
Obsoletes:      python3.11-gnupg < 0.5.3-2
Obsoletes:      python3.11-googleapis-common-protos < 1.65.0-2
Obsoletes:      python3.11-grpcio < 1.68.1-2
Obsoletes:      python3.11-idna < 3.10-2
Obsoletes:      python3.11-idna-ssl < 1.2
Obsoletes:      python3.11-importlib-metadata < 6.0.1-6
Obsoletes:      python3.11-importlib-resources < 6.4.5-2
Obsoletes:      python3.11-inflection < 0.5.1-8
Obsoletes:      python3.11-iniparse < 0.4-40
Obsoletes:      python3.11-jinja2 < 3.1.5-2
Obsoletes:      python3.11-jq < 1.8.0-2
Obsoletes:      python3.11-json_stream < 2.3.3-2
Obsoletes:      python3.11-json_stream_rs_tokenizer < 0.4.27-2
Obsoletes:      python3.11-lockfile < 0.12.2-5
Obsoletes:      python3.11-lxml < 5.3.0-2
Obsoletes:      python3.11-markuppy < 1.14-8
Obsoletes:      python3.11-markupsafe < 2.1.2-5
Obsoletes:      python3.11-mccabe < 0.7.0-5
Obsoletes:      python3.11-multidict < 6.1.0-2
Obsoletes:      python3.11-odfpy < 1.4.1-11
Obsoletes:      python3.11-openpyxl < 3.1.5-2
Obsoletes:      python3.11-packaging < 23.2-2
Obsoletes:      python3.11-parsley < 1.3-7
Obsoletes:      python3.11-pbr < 6.1.0-2
Obsoletes:      python3.11-pexpect < 4.8.0-6
Obsoletes:      python3.11-pillow < 12.1.1-2
Obsoletes:      python3.11-productmd < 1.33-8
Obsoletes:      python3.11-propcache < 0.2.1-2
Obsoletes:      python3.11-protobuf < 4.25.5-2
Obsoletes:      python3.11-psycopg < 3.2.3-2
Obsoletes:      python3.11-psycopg_c < 3.2.3-2
Obsoletes:      python3.11-ptyprocess < 0.7.0-4
Obsoletes:      python3.11-pyOpenSSL < 25.1.0-0.4
Obsoletes:      python3.11-pycares < 4.5.0-2
Obsoletes:      python3.11-pycparser < 2.22-2
Obsoletes:      python3.11-pycryptodomex < 3.20.0-2
Obsoletes:      python3.11-pyflakes < 3.1.0-2
Obsoletes:      python3.11-pygtrie < 2.5.0-6
Obsoletes:      python3.11-pyjwkest < 1.4.2-9
Obsoletes:      python3.11-pyjwt < 2.9.0-2
Obsoletes:      python3.11-pyparsing < 3.1.4-2
Obsoletes:      python3.11-pyrsistent < 0.18.1-7
Obsoletes:      python3.11-pytz < 2022.2.1-7
Obsoletes:      python3.11-pyyaml < 6.0.2-2
Obsoletes:      python3.11-redis < 5.0.8-2
Obsoletes:      python3.11-requests < 2.32.3-3
Obsoletes:      python3.11-requirements-parser < 0.2.0-8
Obsoletes:      python3.11-rhsm < 1.19.2-8
Obsoletes:      python3.11-ruamel-yaml < 0.18.9-2
Obsoletes:      python3.11-ruamel-yaml-clib < 0.2.12-2
Obsoletes:      python3.11-schema < 0.7.7-2
Obsoletes:      python3.11-semantic-version < 2.10.0-6
Obsoletes:      python3.11-six < 1.17.0-2
Obsoletes:      python3.11-smmap < 5.0.1-2
Obsoletes:      python3.11-solv < 0.7.28-2
Obsoletes:      python3.11-tablib < 3.5.0-2
Obsoletes:      python3.11-tenacity < 7.0.0-8
Obsoletes:      python3.11-toml < 0.10.2-8
Obsoletes:      python3.11-tomli_w < 1.2.0-2
Obsoletes:      python3.11-types-cryptography < 3.3.23.2-4
Obsoletes:      python3.11-typing-extensions < 4.12.2-2
Obsoletes:      python3.11-uritemplate < 4.1.1-7
Obsoletes:      python3.11-url-normalize < 1.4.3-9
Obsoletes:      python3.11-urllib3 < 2.6.3-0.2
Obsoletes:      python3.11-urlman < 2.0.1-6
Obsoletes:      python3.11-uuid6 < 2024.7.10-2
Obsoletes:      python3.11-wcmatch < 8.3-6
Obsoletes:      python3.11-webencodings < 0.5.1-7
Obsoletes:      python3.11-whitenoise < 6.7.0-2
Obsoletes:      python3.11-wrapt < 1.17.2-2
Obsoletes:      python3.11-xlrd < 2.0.1-10
Obsoletes:      python3.11-xlwt < 1.3.0-8
Obsoletes:      python3.11-yarl < 1.15.2-2
Obsoletes:      python3.11-zipp < 3.20.2-2

## EL10 transition - additional python3.11 Obsoletes for removed packages

Obsoletes:      python3.11-azure-storage-common < 2.1.0-8
Obsoletes:      python3.11-bleach-whitelist < 0.0.11-8
Obsoletes:      python3.11-box < 5.1.0-8
Obsoletes:      python3.11-cchardet < 2.1.7-6
Obsoletes:      python3.11-coreapi < 2.3.3-9
Obsoletes:      python3.11-coreschema < 0.0.4-9
Obsoletes:      python3.11-django-picklefield < 3.0.1-7
Obsoletes:      python3.11-dotenv < 0.14.0-12
Obsoletes:      python3.11-drf-yasg < 1.17.1-8
Obsoletes:      python3.11-exceptiongroup < 1.1.2-5
Obsoletes:      python3.11-filecache < 0.81-6
Obsoletes:      python3.11-galaxy-ng < 4.5.2-3
Obsoletes:      python3.11-itypes < 1.2.0-8
Obsoletes:      python3.11-jdcal < 1.4.1-8
Obsoletes:      python3.11-marshmallow < 3.13.0-7
Obsoletes:      python3.11-msrest < 0.6.21-7
Obsoletes:      python3.11-naya < 1.1.1-8
Obsoletes:      python3.11-oauthlib < 3.1.1-7
Obsoletes:      python3.11-psycopg2 < 2.9.3-7
Obsoletes:      python3.11-pyperclip < 1.8.2-6
Obsoletes:      python3.11-python3-openid < 3.2.0-7
Obsoletes:      python3.11-requests-oauthlib < 1.3.0-7
Obsoletes:      python3.11-rq < 1.9.0-8
Obsoletes:      python3.11-social-auth-app-django < 3.4.0-7
Obsoletes:      python3.11-social-auth-core < 3.4.0-7

## EL10 transition - python3.12 Obsoletes for removed packages

Obsoletes:      python3.12-async-timeout < 4.0.3-3
Obsoletes:      python3.12-bleach < 3.3.1-8
Obsoletes:      python3.12-bleach-allowlist < 1.0.3-9
Obsoletes:      python3.12-django-auth-ldap < 4.0.0-7
Obsoletes:      python3.12-django-cleanup < 5.1.0-9
Obsoletes:      python3.12-django-guardian < 2.4.0-11
Obsoletes:      python3.12-django-ipware < 3.0.7-8
Obsoletes:      python3.12-django-prometheus < 2.1.0-9
Obsoletes:      python3.12-django-storages < 1.14.6-2
Obsoletes:      python3.12-enrich < 1.2.6-12
Obsoletes:      python3.12-html5lib < 1.1-7
Obsoletes:      python3.12-oauthlib < 3.1.1-7
Obsoletes:      python3.12-python3-openid < 3.2.0-7
Obsoletes:      python3.12-requests-oauthlib < 1.3.0-7
Obsoletes:      python3.12-setuptools_scm_git_archive < 1.4.1-6
Obsoletes:      python3.12-social-auth-app-django < 3.4.0-7
Obsoletes:      python3.12-social-auth-core < 3.4.0-7
Obsoletes:      python3.12-tenacity < 7.0.0-9
Obsoletes:      python3.12-webencodings < 0.5.1-9
Obsoletes:      python3.12-xlrd < 2.0.2-2
Obsoletes:      python3.12-xlwt < 1.3.0-9

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 1.5.0-2
- Bump release for EL10 rebuild
- Drop erroneous Obsoletes for python3.12-lazy-imports: it is a real
  Requires-Dist of python-pulpcore-client and python-pulp-rpm-client,
  wrongly removed as unused in #2766; re-added at 1.2.0-2

* Wed Jul 22 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.5.0-1
- Add Obsoletes for packages removed during EL10 transition

* Thu May 21 2026 Odilon Sousa <osousa@redhat.com> - 1.4.0-1
- Obsolete python3.11 pulpcore packages to clear old installations

* Fri Apr 25 2025 Odilon Sousa <osousa@redhat.com> - 1.3.0-1
- Obsolete unneeded opentelemetry packages after python3.12 rebuild

* Tue Apr 16 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.2.0-1
- Obsolete python3-pulp-2to3-migration & mongo deps

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 1.1.0-1
- Release pulpcore-obsolete-packages 1.1.0
- Bump version for Pulpcore 3.49 Release

* Wed Mar 06 2024 Patrick Creech <pcreech@redhat.com> - 1.0-9
- Increase python39-aiohttp obsolete version to fix upgrades

* Thu Jan 11 2024 Patrick Creech <pcreech@redhat.com> - 1.0-8
- Obsolete aiohttp-socks and pypi-simple as well

* Wed Jan 10 2024 Patrick Creech <pcreech@redhat.com> - 1.0-7
- Obsolete packages to ensure consistent upgrads in older systems

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 1.0-6
- Dont obsolete pyyaml

* Fri Dec 08 2023 Patrick Creech <pcreech@redhat.com> - 1.0-5
- Add django-guardian and importlib-resources to obsoletes

* Wed Nov 22 2023 Patrick Creech <pcreech@redhat.com> - 1.0-4
- Don't obsolete python3-pyyaml

* Wed Nov 22 2023 Patrick Creech <pcreech@redhat.com> - 1.0-3
- Obsolete the python39 pyyaml, as ansible brings in a pyyaml newer than the one we provide

* Mon Aug 28 2023 Odilon Sousa <osousa@redhat.com> - 1.0-2
- Pin the version of django-currentuser

* Tue Aug 15 2023 Zach Huntington-Meath <zhunting@redhat.com> - 1.0-1
- Initial package
