%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name setuptools-scm

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.5.0
Release:        3%{?dist}
Summary:        the blessed package to manage your versions by scm tags

License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-toml


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n setuptools_scm-%{version}
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
%{python3_sitelib}/setuptools_scm
%{python3_sitelib}/setuptools_scm-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Apr 21 2022 Yanis Guenane - 3.5.0-3
- Build against Python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.5.0-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov - 3.5.0-1
- Release python-setuptools-scm 3.5.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.3-2
- Bump release to build for el8

* Wed Jan 29 2020 Evgeni Golov 3.4.3-1
- Update to 3.4.3

* Fri Nov 15 2019 Evgeni Golov - 3.3.3-1
- Initial package.
