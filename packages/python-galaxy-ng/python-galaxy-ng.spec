%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-ng
%global real_version 4.5.2

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.5.2
Release:        3%{?dist}
Summary:        galaxy-ng plugin for the Pulp Project

License:        GPLv2+
URL:            https://github.com/ansible/galaxy_ng/
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{real_version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-automated-logging = 6.1.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-prometheus >= 2.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-auth-ldap = 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-spectacular
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dynaconf >= 3.1.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-galaxy-importer = 0.4.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-ansible < 1:0.14.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-ansible >= 1:0.13.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-container < 2.11.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-container >= 2.10.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.19.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.18.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-social-auth-app-django < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-social-auth-app-django >= 3.1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-social-auth-core < 4.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-social-auth-core >= 3.3.1

Provides:       pulpcore-plugin(galaxy-ng) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{real_version}
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
%{python3_sitelib}/galaxy_ng
%{python3_sitelib}/galaxy_ng-%{real_version}-py%{python3_version}.egg-info


%changelog
* Wed Aug 31 2022 Odilon Sousa <osousa@redhat.com> - 4.5.2-3
- Fixing requirement for pulp-ansible

* Tue Aug 30 2022 Odilon Sousa <osousa@redhat.com> - 4.5.2-2
- Removing python-naya requirement, it was added on galaxy-ng, but it's a
  requirement for pulpcore

* Wed Aug 24 2022 Odilon Sousa <osousa@redhat.com> - 4.5.2-1
- Release python-galaxy-ng 4.5.2

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 4.5.0-2
- Obsolete the old Python 3.8 package for smooth upgrade

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 4.5.0-1
- Release python-galaxy-ng 4.5.0

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 4.5.0-0.1.b1
- Release python-galaxy-ng 4.5.0b1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.4.0-0.3.b1
- Build against python 3.9

* Wed Oct 20 2021 Odilon Sousa <osousa@redhat.com> - 4.4.0-0.2.b1
- Release python-galaxy-ng 4.4.0b1

* Mon Oct 18 2021 Evgeni Golov - 4.4.0-0.2.a2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 27 2021 Evgeni Golov 4.4.0-0.1.a2
- Update to 4.4.0a2

* Mon Sep 13 2021 Evgeni Golov 4.4.0-0.1.a1
- Update to 4.4.0a1

* Fri Jun 04 2021 Evgeni Golov - 4.3.1-1
- Release python-galaxy-ng 4.3.1

* Wed Jun 02 2021 Evgeni Golov 4.3.0-1
- Update to 4.3.0

* Wed May 12 2021 Evgeni Golov 4.3.0-0.1.b4
- Update to 4.3.0b4

* Mon Apr 19 2021 Evgeni Golov 4.3.0-0.1.a2
- Update to 4.3.0a2

* Thu Apr 01 2021 Evgeni Golov 4.3.0-0.1.a1
- Update to 4.3.0a1

* Fri Dec 18 2020 Evgeni Golov - 4.2.1-1
- Release python-galaxy-ng 4.2.1

* Fri Nov 13 2020 Evgeni Golov 4.2.0-1
- Update to 4.2.0

* Thu Nov 05 2020 Evgeni Golov 4.2.0-0.1.rc3
- Update to 4.2.0rc3

* Tue Nov 03 2020 Evgeni Golov 4.2.0-0.1.rc2
- Update to 4.2.0rc2

* Mon Oct 05 2020 Evgeni Golov 4.2.0-0.1.rc1
- Update to 4.2.0rc1

* Mon Sep 28 2020 Evgeni Golov 4.2.0-0.1.b3
- Update to 4.2.0b3

* Thu Sep 17 2020 Evgeni Golov 4.2.0-0.1.b2
- Update to 4.2.0b2

* Mon Sep 14 2020 Evgeni Golov 4.2.0-0.1.b1
- Update to 4.2.0b1

* Fri Jul 17 2020 Evgeni Golov - 4.2.0-0.1.a10
- Initial package.
