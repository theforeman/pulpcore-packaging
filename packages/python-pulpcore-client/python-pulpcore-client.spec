%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.28.24
Release:        1%{?dist}
Summary:        Pulp 3 API

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-certifi
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-dateutil
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.15


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
%autosetup -n %{pypi_name}-%{version}
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
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulpcore_client-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Mar 21 2024 Odilon Sousa <osousa@redhat.com> - 3.28.24-1
- Release python-pulpcore-client 3.28.24

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
