%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name python-dateutil
%global srcname dateutil

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.8.2
Release:        2%{?dist}
Summary:        Extensions to the standard Python datetime module

License:        Dual License
URL:            https://dateutil.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.5


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.5
Obsoletes:      %{?scl_prefix}python36-dateutil


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/dateutil
%{python3_sitelib}/python_dateutil-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 26 2022 Yanis Guenane - 2.8.2-2
- Build against Python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.8.2-1
- Release python-dateutil 2.8.2

* Wed Sep 08 2021 Evgeni Golov - 2.8.1-4
- Build against Python 3.8

* Mon Aug 24 2020 Evgeni Golov - 2.8.1-3
- Fix Obsoletes

* Thu Aug 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.8.1-2
- Obsolete python36-dateutil

* Fri Jul 17 2020 Evgeni Golov - 2.8.1-1
- Initial package.
