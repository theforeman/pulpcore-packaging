%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore-client

Name:           python-%{pypi_name}
Version:        3.49.19
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-certifi
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six >= 1.10
BuildRequires:  python%{python3_pkgversion}-urllib3 >= 1.15


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-certifi
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-six >= 1.10
Requires:       python%{python3_pkgversion}-urllib3 >= 1.15

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulpcore_client-%{version}-py%{python3_version}.egg-info


%changelog
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
