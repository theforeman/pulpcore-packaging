%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name python-debian
%global srcname debian

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.1.40
Release:        2%{?dist}
Summary:        Debian package related modules

License:        GPL-2+
URL:            https://salsa.debian.org/python-debian-team/python-debian
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-chardet
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-chardet
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six


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
%doc README.rst
%{python3_sitelib}/__pycache__/deb822.*
%{python3_sitelib}/deb822.py
%{python3_sitelib}/debian
%{python3_sitelib}/debian_bundle
%{python3_sitelib}/python_debian-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 08 2021 Evgeni Golov - 0.1.40-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 0.1.40-1
- Update to 0.1.40

* Fri Mar 19 2021 Evgeni Golov 0.1.39-1
- Update to 0.1.39

* Thu Oct 29 2020 Evgeni Golov 0.1.38-1
- Update to 0.1.38

* Thu Apr 30 2020 Markus Bucher <bucher@atix.de> - 0.1.37-1
- Initial package.
