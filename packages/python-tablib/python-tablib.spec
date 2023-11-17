%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name tablib

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.3.0
Release:        3%{?dist}
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:        MIT
URL:            https://tablib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markuppy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-odfpy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-openpyxl >= 2.6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyyaml
Requires:       %{?scl_prefix}python%{python3_pkgversion}-xlrd
Requires:       %{?scl_prefix}python%{python3_pkgversion}-xlwt

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.3.0-1
- Update to 3.3.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 3.2.0-1
- Release python-tablib 3.2.0

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.1.0-1
- Release python-tablib 3.1.0

* Tue Oct 19 2021 Evgeni Golov - 3.0.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.0.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Jun 04 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Tue Apr 28 2020 Evgeni Golov - 1.1.0-1
- Initial package.
