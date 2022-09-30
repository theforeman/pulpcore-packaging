%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-python

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.7.2
Release:        2%{?dist}
Summary:        pulp-python plugin for the Pulp Project

License:        GPLv2+
URL:            https://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-bandersnatch >= 5.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-bandersnatch >= 5.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging >= 21.3
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-packaging >= 22.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pkginfo >= 1.8.2
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-pkginfo >= 1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.17
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-pulpcore > 3.25
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pypi-simple >= 0.9
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-pypi-simple >= 0.10

Provides:       pulpcore-plugin(python) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

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
%license LICENSE
%doc README.md
%{python3_sitelib}/pulp_python
%{python3_sitelib}/pulp_python-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 3.7.2-2
- Fixing operator logic on Conflicts for pulpcore

* Tue Sep 20 2022 Odilon Sousa 3.7.2-1
- Update to 3.7.2

* Thu Jun 30 2022 Ian Ballou <ianballou67@gmail.com> - 3.7.1-1
- Release pulp-python 3.7.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.6.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.6.0-4
- Build against python 3.9

* Wed Feb 23 2022 Odilon Sousa <osousa@redhat.com> - 3.6.0-3
- Adding pypi-simple as dependency

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 3.6.0-2
- Fixup dependency issues

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.6.0-1
- Release python-pulp-python 3.6.0

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 3.5.2-1
- Release python-pulp-python 3.5.2

* Mon Oct 18 2021 Evgeni Golov - 3.5.1-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 3.5.1-1
- Update to 3.5.1

* Wed Sep 08 2021 Evgeni Golov 3.5.0-1
- Update to 3.5.0

* Tue Jul 13 2021 Evgeni Golov - 3.4.0-1
- Initial package.
