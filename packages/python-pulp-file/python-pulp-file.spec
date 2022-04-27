%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-file

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.10.2
Release:        1%{?dist}
Summary:        File plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
A Pulp plugin to support hosting arbitrary files.


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.20
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.16.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(file) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
A Pulp plugin to support hosting arbitrary files.


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_file
%{python3_sitelib}/pulp_file-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 1.10.2-1
- Release python-pulp-file 1.10.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.10.1-3
- Build against python 3.9

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 1.10.1-2
- Fixup dependency issues

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 1.10.1-1
- Release python-pulp-file 1.10.1

* Mon Oct 18 2021 Evgeni Golov - 1.9.1-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Wed Sep 08 2021 Evgeni Golov 1.9.1-1
- Update to 1.9.1

* Tue Aug 17 2021 Odilon Sousa <osousa@redhat.com> - 1.8.2-1
- Release python-pulp-file 1.8.2

* Fri Jul 02 2021 Evgeni Golov - 1.8.1-1
- Release python-pulp-file 1.8.1

* Tue Jun 29 2021 Evgeni Golov - 1.8.0-1
- Release python-pulp-file 1.8.0

* Fri Jun 11 2021 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Fri Mar 19 2021 Evgeni Golov 1.6.0-1
- Update to 1.6.0

* Mon Jan 11 2021 Evgeni Golov 1.5.0-1
- Update to 1.5.0

* Mon Sep 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Tue Aug 25 2020 Evgeni Golov 1.2.0-1
- Update to 1.2.0

* Thu Jun 04 2020 Evgeni Golov 1.0.1-1
- Update to 1.0.1

* Tue Apr 28 2020 Evgeni Golov 0.3.0-1
- Update to 0.3.0

* Wed Mar 18 2020 Samir Jha 0.2.0-1
- Update to 0.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.1-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 0.1.1-1
- Update to 0.1.1

* Fri Dec 13 2019 Evgeni Golov 0.1.0-1
- Update to 0.1.0

* Mon Nov 18 2019 Evgeni Golov - 0.1.0rc1-1
- Initial package.
