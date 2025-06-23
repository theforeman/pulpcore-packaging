%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm-client
%global src_name pulp_rpm_client

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.29.4
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pulp_rpm-client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros



Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-urllib3 >= 1.15

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n pulp_rpm-client-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%exclude %{python3_sitelib}/pulpcore/__pycache__/*
%exclude %{python3_sitelib}/pulpcore/__init__.py
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_rpm_client-%{version}.dist-info/


%changelog
* Mon Jun 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.4-1
- Update to 3.29.4

* Tue Jun 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.3-1
- Update to 3.29.3

* Thu Apr 24 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.2-1
- Update to 3.29.2

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 3.29.1-2
- Add obsoletes for python3.11 package

* Fri Apr 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.1-1
- Update to 3.29.1

* Mon Mar 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.29.0-1
- Update to 3.29.0

* Thu Oct 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.2-1
- Update to 3.27.2

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.27.1-1
- Update to 3.27.1

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 3.25.4-1
- Release python-pulp-rpm-client 3.25.4

* Thu Apr 18 2024 Odilon Sousa <osousa@redhat.com> - 3.25.3-1
- Release python-pulp-rpm-client 3.25.3

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.25.1-1
- Release python-pulp-rpm-client 3.25.1

* Wed Mar 06 2024 Odilon Sousa <osousa@redhat.com> - 3.23.3-1
- Release python-pulp-rpm-client 3.23.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.23.0-3
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.23.0-2
- Obsolete python39 packages for a smooth upgrade

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 3.23.0-1
- Release python-pulp-rpm-client 3.23.0

* Wed Oct 18 2023 Odilon Sousa <osousa@redhat.com> - 3.22.6-1
- Release python-pulp-rpm-client 3.22.6

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 3.22.3-1
- Release python-pulp-rpm-client 3.22.3

* Mon Mar 20 2023 Odilon Sousa <osousa@redhat.com> - 3.19.2-1
- Release python-pulp-rpm-client 3.19.2

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.18.10-1
- Release python-pulp-rpm-client 3.18.10

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-1
- Release python-pulp-rpm-client 3.18.5

* Tue Sep 20 2022 Odilon Sousa - 3.18.1-1
- Update to 3.18.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.3-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.17.3-1
- Release python-pulp-rpm-client 3.17.3

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 3.16.1-1
- Release python-pulp-rpm-client 3.16.1

* Wed Sep 08 2021 Evgeni Golov - 3.15.0-1
- Update to 3.15.0

* Thu Jul 08 2021 Evgeni Golov - 3.13.3-1
- Release python-pulp-rpm-client 3.13.3

* Tue Jun 29 2021 Evgeni Golov - 3.13.2-1
- Release python-pulp-rpm-client 3.13.2

* Thu Jun 17 2021 Evgeni Golov - 3.12.0-1
- Release python-pulp-rpm-client 3.12.0

* Fri May 21 2021 Evgeni Golov - 3.11.0-1
- Initial package.
