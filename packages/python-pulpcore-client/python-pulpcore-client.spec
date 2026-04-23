%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore-client
%global src_name pulpcore_client

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.105.4
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-six >= 1.10
Requires:       python%{python3_pkgversion}-urllib3 >= 1.15

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulpcore_client-%{version}.dist-info/


%changelog
* Thu Apr 23 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.105.4-1
- Update to 3.105.4

* Fri Apr 17 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.105.3-1
- Update to 3.105.3

* Tue Apr 14 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.105.0-1
- Update to 3.105.0

* Mon Mar 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.12-1
- Update to 3.85.12
- Fix Source0: tarball uses underscores (pulpcore_client) since 3.85.x

* Mon Sep 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.85.1-1
- Update to 3.85.1

* Wed Sep 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.15-1
- Update to 3.73.15

* Mon Jun 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.14-1
- Update to 3.73.14

* Wed Jun 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.12-1
- Update to 3.73.12

* Thu Jun 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.11-1
- Update to 3.73.11

* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.9-1
- Update to 3.73.9

* Mon May 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.8-1
- Update to 3.73.8

* Thu Apr 24 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.7-1
- Update to 3.73.7

* Fri Apr 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.73.4-1
- Update to 3.73.4

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 3.73.2-2
- Add obsoletes for python3.11 package

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

* Thu Nov 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.4-1
- Update to 3.63.4

* Thu Nov 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.3-1
- Update to 3.63.3

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.2-1
- Update to 3.63.2

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.1-1
- Update to 3.63.1

* Tue Oct 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.0-1
- Update to 3.63.0

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.20-1
- Update to 3.49.20

* Tue Sep 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.19-1
- Update to 3.49.19

* Mon Aug 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.17-1
- Update to 3.49.17

* Wed Aug 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.16-1
- Update to 3.49.16

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 3.49.15-1
- Release python-pulpcore-client 3.49.15

* Mon Jul 22 2024 Odilon Sousa <osousa@redhat.com> - 3.49.14-1
- Release python-pulpcore-client 3.49.14

* Mon May 27 2024 Odilon Sousa <osousa@redhat.com> - 3.49.10-1
- Release python-pulpcore-client 3.49.10

* Wed May 22 2024 Odilon Sousa <osousa@redhat.com> - 3.49.9-1
- Release python-pulpcore-client 3.49.9

* Tue May 14 2024 Odilon Sousa <osousa@redhat.com> - 3.49.7-1
- Release python-pulpcore-client 3.49.7

* Fri Apr 26 2024 Odilon Sousa <osousa@redhat.com> - 3.49.5-1
- Release python-pulpcore-client 3.49.5

* Wed Mar 27 2024 Odilon Sousa <osousa@redhat.com> - 3.49.3-1
- Release python-pulpcore-client 3.49.3

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.49.1-1
- Release python-pulpcore-client 3.49.1

* Tue Mar 05 2024 Odilon Sousa <osousa@redhat.com> - 3.39.11-1
- Release python-pulpcore-client 3.39.11

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 3.39.8-1
- Release python-pulpcore-client 3.39.8

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.39.4-2
- Remove SCL bits

* Wed Jan 03 2024 Odilon Sousa <osousa@redhat.com> - 3.39.4-1
- Release python-pulpcore-client 3.39.4

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.39.2-2
- Obsolete python39 packages for a smooth upgrade

* Wed Nov 08 2023 Odilon Sousa <osousa@redhat.com> - 3.39.2-1
- Release python-pulpcore-client 3.39.2

* Mon Nov 06 2023 Odilon Sousa <osousa@redhat.com> - 3.28.19-1
- Release python-pulpcore-client 3.28.19

* Wed Oct 18 2023 Odilon Sousa <osousa@redhat.com> - 3.28.18-1
- Release python-pulpcore-client 3.28.18

* Mon Oct 02 2023 Odilon Sousa <osousa@redhat.com> - 3.28.16-1
- Release python-pulpcore-client 3.28.16

* Wed Sep 20 2023 Odilon Sousa <osousa@redhat.com> - 3.28.15-1
- Release python-pulpcore-client 3.28.15

* Thu Aug 31 2023 Odilon Sousa <osousa@redhat.com> - 3.28.10-1
- Release python-pulpcore-client 3.28.10

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 3.28.5-1
- Release python-pulpcore-client 3.28.5

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-1
- Release python-pulpcore-client 3.22.2

* Tue Sep 20 2022 Odilon Sousa - 3.21.0-1
- Update to 3.21.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.3-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.17.3-1
- Release python-pulpcore-client 3.17.3

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 3.16.0-1
- Release python-pulpcore-client 3.16.0

* Wed Sep 08 2021 Evgeni Golov - 3.15.2-1
- Update to 3.15.2

* Thu Jul 08 2021 Evgeni Golov - 3.14.1-1
- Release python-pulpcore-client 3.14.1

* Thu Jun 17 2021 Evgeni Golov - 3.13.0-1
- Release python-pulpcore-client 3.13.0

* Fri May 21 2021 Evgeni Golov - 3.11.1-1
- Initial package.
