#!/usr/bin/env python3

import unittest
import sys
import os

# Add the parent directory to the path so we can import find_package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from find_package import parse_package_list


class TestIntegration(unittest.TestCase):
    
    def test_real_world_sample_data(self):
        """Test with actual sample data from the user to verify correct transformations"""
        # This is a subset of the actual data provided by the user
        test_input = [
            "aiodns==3.2.0",
            "aiofiles==24.1.0", 
            "aiohappyeyeballs==2.6.1",
            "aiohttp==3.11.18",
            "aiohttp-xmlrpc==1.5.0",
            "aiohttp_socks==0.10.1",
            "aiosignal==1.4.0",
            "annotated-types==0.7.0",
            "anyio==4.9.0",
            "asgiref==3.9.0",
            "async-lru==2.0.5",
            "asyncio-throttle==1.0.2",
            "attrs==22.2.0",
            "azure-core==1.35.0",
            "azure-storage-blob==12.25.1",
            "backoff==2.2.1",
            "bandersnatch==6.3.0",
            "beautifulsoup4==4.13.4",
            "bindep==2.13.0",
            "boto3==1.39.3",
            "botocore==1.39.3",
            "bracex==2.6",
            "build==1.2.2.post1",
            "CacheControl==0.14.3",
            "cachetools==5.5.2",
            "certifi==2025.6.15",
            "cffi==1.17.1",
            "charset-normalizer==3.4.2",
            "cleo==2.1.0",
            "click==8.1.8",
            "crashtest==0.4.1",
            "cryptography==45.0.4",
            "defusedxml==0.7.1",
            "Deprecated==1.2.18",
            "diff-match-patch==20241021",
            "distlib==0.3.9",
            "Django==4.2.23",
            "django-filter==25.1",
            "django-guid==3.5.1",
            "django-import-export==3.3.9",
            "django-lifecycle==1.2.4",
            "django-readonly-field==1.1.2",
            "django-storages==1.14.6",
            "djangorestframework==3.15.2",
            "djangorestframework-queryfields==1.1.0",
            "docutils==0.21.2",
            "drf-access-policy==1.5.0",
            "drf-nested-routers==0.94.1",
            "drf-spectacular==0.27.2",
            "dulwich==0.21.7",
            "dynaconf==3.2.11",
            "editables==0.5",
            "et_xmlfile==2.0.0",
            "fastjsonschema==2.21.1",
            "filelock==3.18.0",
            "flake8==6.1.0",
            "flit==3.12.0",
            "flit_core==3.12.0",
            "frozenlist==1.7.0",
            "galaxy_importer==0.4.31",
            "gitdb==4.0.12",
            "GitPython==3.1.44",
            "google-api-core==2.25.1",
            "google-auth==2.40.3",
            "google-cloud-core==2.4.3",
            "google-cloud-storage==3.1.1",
            "google-crc32c==1.7.1",
            "google-resumable-media==2.7.2",
            "googleapis-common-protos==1.70.0",
            "gunicorn==23.0.0",
            "h11==0.16.0",
            "hatch==1.9.7",
            "hatchling==1.21.1",
            "httpcore==1.0.9",
            "httpx==0.28.1",
            "humanfriendly==10.0",
            "hyperlink==21.0.0",
            "idna==3.10",
            "importlib-metadata==6.0.1",
            "importlib_resources==6.4.5",
            "inflection==0.5.1",
            "installer==0.7.0",
            "isodate==0.7.2",
            "jaraco.classes==3.4.0",
            "jeepney==0.9.0",
            "Jinja2==3.1.6",
            "jmespath==1.0.1",
            "jq==1.8.0",
            "json-stream==2.3.3",
            "json-stream-rs-tokenizer==0.4.29",
            "keyring==24.3.1",
            "lxml==6.0.0",
            "Markdown==3.8.2",
            "MarkupPy==1.18",
            "MarkupSafe==3.0.2",
            "maturin==1.9.0",
            "mccabe==0.7.0",
            "more-itertools==10.7.0",
            "msgpack==1.1.1",
            "multidict==6.4.4",
            "mypy_extensions==1.1.0",
            "nh3==0.2.21",
            "odfpy==1.4.1",
            "openpyxl==3.1.5",
            "opentelemetry-api==1.30.0",
            "opentelemetry-exporter-otlp-proto-common==1.30.0",
            "opentelemetry-exporter-otlp-proto-http==1.30.0",
            "opentelemetry-proto==1.30.0",
            "opentelemetry-sdk==1.30.0",
            "opentelemetry-semantic-conventions==0.51b0",
            "packaging==24.2",
            "Parsley==1.3",
            "pathspec==0.12.1",
            "pbr==6.1.1",
            "pexpect==4.9.0",
            "pillow==11.1.0",
            "pkginfo==1.12.1.2",
            "platformdirs==4.3.8",
            "pluggy==1.6.0",
            "poetry==1.8.3",
            "poetry-core==1.9.0",
            "poetry-plugin-export==1.8.0",
            "productmd==1.33",
            "propcache==0.3.2",
            "proto-plus==1.26.1",
            "protobuf==5.29.5",
            "psycopg==3.2.9",
            "psycopg-c==3.2.9",
            "ptyprocess==0.7.0",
            "pyasn1==0.6.1",
            "pyasn1_modules==0.4.2",
            "pycairo==1.28.0",
            "pycares==4.9.0",
            "pycodestyle==2.11.1",
            "pycparser==2.22",
            "pydantic==2.11.7",
            "pydantic_core==2.33.2",
            "pyflakes==3.1.0",
            "Pygments==2.19.2",
            "PyGObject==3.50.1",
            "pygtrie==2.5.0",
            "PyJWT==2.10.1",
            "pyOpenSSL==25.1.0",
            "pyparsing==3.2.1",
            "pypi-simple==1.6.1",
            "pyproject_hooks==1.2.0",
            "python-dateutil==2.9.0.post0",
            "python-debian==0.1.49",
            "python-gnupg==0.5.4",
            "python-socks==2.7.1",
            "PyYAML==6.0.2",
            "RapidFuzz==3.13.0",
            "redis==5.2.1",
            "requests==2.32.4",
            "requests-toolbelt==1.0.0",
            "rich==14.0.0",
            "rsa==4.9.1",
            "ruamel.yaml==0.18.14",
            "ruamel.yaml.clib==0.2.12",
            "s3transfer==0.13.0",
            "schema==0.7.7",
            "SecretStorage==3.3.3",
            "semantic-version==2.10.0",
            "setuptools==68.2.2",
            "shellingham==1.5.4",
            "six==1.17.0",
            "smmap==5.0.2",
            "sniffio==1.3.1",
            "soupsieve==2.7",
            "sqlparse==0.5.3",
            "tablib==3.5.0",
            "tomli_w==1.2.0",
            "tomlkit==0.13.3",
            "trove-classifiers==2025.5.9.12",
            "typing-inspection==0.4.1",
            "typing_extensions==4.14.1",
            "uritemplate==4.2.0",
            "url-normalize==1.4.3",
            "urllib3==2.5.0",
            "userpath==1.9.2",
            "uuid6==2024.7.10",
            "virtualenv==20.25.3",
            "wcmatch==10.1",
            "wheel==0.41.2",
            "whitenoise==6.9.0",
            "wrapt==1.17.2",
            "xlrd==2.0.2",
            "xlwt==1.3.0",
            "yarl==1.18.3",
            "zipp==3.23.0",
            "zstandard==0.23.0"
        ]
        
        # Parse the input
        result = list(parse_package_list(test_input))
        
        # Check specific transformations that we expect
        result_dict = {pkg['package_name']: pkg['new_version'] for pkg in result}
        
        # Test key transformations
        self.assertEqual(result_dict['aiohttp-socks'], '0.10.1')  # aiohttp_socks -> aiohttp-socks
        self.assertEqual(result_dict['cachecontrol'], '0.14.3')  # CacheControl -> cachecontrol
        self.assertEqual(result_dict['deprecated'], '1.2.18')  # Deprecated -> deprecated
        self.assertEqual(result_dict['django'], '4.2.23')  # Django -> django
        self.assertEqual(result_dict['et-xmlfile'], '2.0.0')  # et_xmlfile -> et-xmlfile
        self.assertEqual(result_dict['flit-core'], '3.12.0')  # flit_core -> flit-core
        self.assertEqual(result_dict['galaxy-importer'], '0.4.31')  # galaxy_importer -> galaxy-importer
        self.assertEqual(result_dict['gitpython'], '3.1.44')  # GitPython -> gitpython
        self.assertEqual(result_dict['importlib-resources'], '6.4.5')  # importlib_resources -> importlib-resources
        self.assertEqual(result_dict['jaraco-classes'], '3.4.0')  # jaraco.classes -> jaraco-classes
        self.assertEqual(result_dict['jinja2'], '3.1.6')  # Jinja2 -> jinja2
        self.assertEqual(result_dict['markuppy'], '1.18')  # MarkupPy -> markuppy
        self.assertEqual(result_dict['markupsafe'], '3.0.2')  # MarkupSafe -> markupsafe
        self.assertEqual(result_dict['opentelemetry_api'], '1.30.0')  # opentelemetry-api -> opentelemetry_api
        self.assertEqual(result_dict['opentelemetry_exporter_otlp_proto_common'], '1.30.0')  # opentelemetry-exporter-otlp-proto-common -> opentelemetry_exporter_otlp_proto_common
        self.assertEqual(result_dict['parsley'], '1.3')  # Parsley -> parsley
        self.assertEqual(result_dict['poetry-core'], '1.9.0')  # poetry-core -> poetry-core
        self.assertEqual(result_dict['poetry-plugin-export'], '1.8.0')  # poetry-plugin-export -> poetry-plugin-export
        self.assertEqual(result_dict['psycopg_c'], '3.2.9')  # psycopg-c -> psycopg_c
        self.assertEqual(result_dict['pyasn1-modules'], '0.4.2')  # pyasn1_modules -> pyasn1-modules
        self.assertEqual(result_dict['pydantic-core'], '2.33.2')  # pydantic_core -> pydantic-core
        self.assertEqual(result_dict['pygments'], '2.19.2')  # Pygments -> pygments
        self.assertEqual(result_dict['pygobject'], '3.50.1')  # PyGObject -> pygobject
        self.assertEqual(result_dict['pyjwt'], '2.10.1')  # PyJWT -> pyjwt
        self.assertEqual(result_dict['dateutil'], '2.9.0.post0')  # python-dateutil -> dateutil
        self.assertEqual(result_dict['debian'], '0.1.49')  # python-debian -> debian
        self.assertEqual(result_dict['gnupg'], '0.5.4')  # python-gnupg -> gnupg
        self.assertEqual(result_dict['socks'], '2.7.1')  # python-socks -> socks
        self.assertEqual(result_dict['pyyaml'], '6.0.2')  # PyYAML -> pyyaml
        self.assertEqual(result_dict['rapidfuzz'], '3.13.0')  # RapidFuzz -> rapidfuzz
        self.assertEqual(result_dict['ruamel-yaml'], '0.18.14')  # ruamel.yaml -> ruamel-yaml
        self.assertEqual(result_dict['ruamel-yaml-clib'], '0.2.12')  # ruamel.yaml.clib -> ruamel-yaml-clib
        self.assertEqual(result_dict['secretstorage'], '3.3.3')  # SecretStorage -> secretstorage
        self.assertEqual(result_dict['typing-extensions'], '4.14.1')  # typing_extensions -> typing-extensions
        
        # Test some packages that should NOT be transformed
        self.assertEqual(result_dict['requests'], '2.32.4')  # requests -> requests (no change)
        self.assertEqual(result_dict['urllib3'], '2.5.0')  # urllib3 -> urllib3 (no change)
        self.assertEqual(result_dict['certifi'], '2025.6.15')  # certifi -> certifi (no change)
        self.assertEqual(result_dict['click'], '8.1.8')  # click -> click (no change)
        self.assertEqual(result_dict['attrs'], '22.2.0')  # attrs -> attrs (no change)
        
        # Verify total count
        self.assertEqual(len(result), len(test_input))
        
        print(f"Successfully processed {len(result)} packages")
        print("Sample transformations verified:")
        print(f"  aiohttp_socks -> {result_dict['aiohttp-socks']}")
        print(f"  CacheControl -> {result_dict['cachecontrol']}")
        print(f"  galaxy_importer -> {result_dict['galaxy-importer']}")
        print(f"  python-dateutil -> {result_dict['dateutil']}")
        print(f"  PyYAML -> {result_dict['pyyaml']}")
        print(f"  opentelemetry-api -> {result_dict['opentelemetry_api']}")


if __name__ == '__main__':
    unittest.main() 