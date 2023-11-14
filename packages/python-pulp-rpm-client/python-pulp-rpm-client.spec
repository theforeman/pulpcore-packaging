%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.23.0
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pulp_rpm-client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-certifi
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dateutil
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.15


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n pulp_rpm-client-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%exclude %{python3_sitelib}/pulpcore/__pycache__/*
%exclude %{python3_sitelib}/pulpcore/__init__.py
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulp_rpm_client-%{version}-py%{python3_version}.egg-info


%changelog
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
