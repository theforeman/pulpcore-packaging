Name: pulpcore-obsolete-packages
Version: 1.0
Release: 3%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/pulpcore-packaging
BuildArch: noarch

Obsoletes:      python3-django-currentuser < 0.5.3-6
Obsoletes:      python3-pyyaml < 6.4.1-5
%if 0%{?rhel} == 8
Obsoletes:      python39-django-currentuser < 0.5.3-6
Obsoletes:      python39-pyyaml < 5.4.1-5
%endif

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Wed Nov 22 2023 Patrick Creech <pcreech@redhat.com> - 1.0-3
- Obsolete the python39 pyyaml, as ansible brings in a pyyaml newer than the one we provide

* Mon Aug 28 2023 Odilon Sousa <osousa@redhat.com> - 1.0-2
- Pin the version of django-currentuser

* Tue Aug 15 2023 Zach Huntington-Meath <zhunting@redhat.com> - 1.0-1
- Initial package
