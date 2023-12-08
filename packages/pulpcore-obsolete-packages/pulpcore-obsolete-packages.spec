Name: pulpcore-obsolete-packages
Version: 1.2.0
Release: 1%{?dist}
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

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
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
