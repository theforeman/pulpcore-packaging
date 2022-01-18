%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pbr

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.8.0
Release:        1%{?dist}
Summary:        Python Build Reasonableness

License:        None
URL:            https://docs.openstack.org/pbr/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-coverage = 4.4
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.6.6
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.6.6
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.6.7
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.6.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage >= 4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-fixtures >= 3.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hacking < 4.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hacking >= 1.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mock < 4.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mock >= 2.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mock >= 2.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pre-commit >= 2.6.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.12.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-stestr < 3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-stestr >= 2.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-stestr >= 2.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-testrepository >= 0.0.18
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-testresources >= 2.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-testscenarios >= 0.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-testtools >= 2.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-virtualenv >= 20.0.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel >= 0.32.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%license LICENSE pbr/tests/testpackage/LICENSE.txt
%doc README.rst pbr/tests/testpackage/README.txt
%{_bindir}/pbr
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 5.8.0-1
- Update to 5.8.0

* Wed Sep 08 2021 Evgeni Golov - 5.6.0-1
- Initial package.
