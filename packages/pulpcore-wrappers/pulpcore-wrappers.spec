%global wrappers gunicorn rq

Name:           pulpcore-wrappers
Version:        1.0.0
Release:        1%{?dist}
Summary:        pulpcore SELinux wrappers

License:        GPL2+
URL:            https://pulpproject.org
Source0:        empty-file

BuildArch:      noarch

Requires:       python3-pulpcore

%description
pulpcore SELinux wrappers

%prep
# nothing

%build
for wrapper in %{wrappers}
do
  printf '#!/bin/bash\nexec %s "$@"\n' ${wrapper} > ${wrapper}
done


%install
for wrapper in %{wrappers}
do
  install -D -m 755 ${wrapper} %{buildroot}%{_libexecdir}/pulpcore/${wrapper}
done

%files
%defattr(-,root,root,0755)
%{_libexecdir}/pulpcore/*


%changelog
* Tue Oct 06 2020 Evgeni Golov - 1.0.0-1
- Initial package
