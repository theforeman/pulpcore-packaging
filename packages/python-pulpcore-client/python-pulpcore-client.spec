%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.22.14
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
* Wed Sep 06 2023 Patrick Creech <pcreech@redhat.com> - 3.22.14-1
- Release python-pulpcore-client 3.22.14

* Wed Aug 09 2023 Patrick Creech <pcreech@redhat.com> - 3.22.12-1
- Release python-pulpcore-client 3.22.12

* Tue Jul 25 2023 Patrick Creech <pcreech@redhat.com> - 3.22.9-1
- Release python-pulpcore-client 3.22.9

* Wed Jun 28 2023 Odilon Sousa <osousa@redhat.com> - 3.22.7-1
- Release python-pulpcore-client 3.22.7

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
