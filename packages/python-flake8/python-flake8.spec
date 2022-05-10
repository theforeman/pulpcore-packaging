%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name flake8

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.9.2
Release:        5%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co

License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mccabe < 0.7.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mccabe >= 0.6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pycodestyle < 2.8.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pycodestyle >= 2.7.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyflakes < 2.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyflakes >= 2.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
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
%doc README.rst tests/fixtures/config_files/README.rst
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.9.2-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.9.2-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 3.9.2-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.9.2-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 3.9.2-1
- Update to 3.9.2

* Fri Mar 19 2021 Evgeni Golov 3.9.0-1
- Update to 3.9.0

* Thu Oct 29 2020 Evgeni Golov 3.8.4-1
- Update to 3.8.4

* Tue Jun 23 2020 Evgeni Golov - 3.8.3-1
- Initial package.
