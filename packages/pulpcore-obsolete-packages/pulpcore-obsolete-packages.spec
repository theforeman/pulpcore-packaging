Name: pulpcore-obsolete-packages
Version: 1.0
Release: 2%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/pulpcore-packaging
BuildArch: noarch

Obsoletes:      python3-django-currentuser < 0.5.3-6
%if 0%{?rhel} == 8
Obsoletes:      python39-django-currentuser < 0.5.3-6
%endif

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Mon Aug 28 2023 Odilon Sousa <osousa@redhat.com> - 1.0-2
- Pin the version of django-currentuser

* Tue Aug 15 2023 Zach Huntington-Meath <zhunting@redhat.com> - 1.0-1
- Initial package
