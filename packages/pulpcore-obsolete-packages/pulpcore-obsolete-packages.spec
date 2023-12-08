Name: pulpcore-obsolete-packages
Version: 1.0
Release: 5%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/pulpcore-packaging
BuildArch: noarch

Obsoletes:      python3-django-currentuser < 0.5.3-6
%if 0%{?rhel} == 8
Obsoletes:      python39-django-currentuser < 0.5.3-6
Obsoletes:      python39-pyyaml < 5.4.1-5
Obsoletes:      python39-importlib-resources < 5.4.0-6
Obsoletes:      python39-django-guardian < 2.4.0-7
%endif

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
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
