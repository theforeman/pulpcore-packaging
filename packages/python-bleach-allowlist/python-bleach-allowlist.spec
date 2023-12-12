%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name bleach-allowlist

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.3
Release:        6%{?dist}
Summary:        Curated lists of tags and attributes for sanitizing html

License:        BSD License
URL:            https://github.com/yourcelf/bleach-allowlist.git
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%doc README.rst
%{python3_sitelib}/bleach_allowlist
%{python3_sitelib}/bleach_allowlist-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.3-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.3-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.3-2
- Build against Python 3.8

* Mon Feb 22 2021 Evgeni Golov - 1.0.3-1
- Release python-bleach-allowlist 1.0.3

* Mon Aug 10 2020 Evgeni Golov 0.0.11-1
- Update to 0.0.11

* Tue Jun 23 2020 Evgeni Golov - 0.0.10-1
- Initial package.
