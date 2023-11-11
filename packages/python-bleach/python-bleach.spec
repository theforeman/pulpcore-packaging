%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name bleach

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.3.1
Release:        3%{?dist}
Summary:        An easy safelist-based HTML-sanitizing tool

License:        Apache Software License
URL:            https://github.com/mozilla/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.9.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-webencodings


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
%doc README.rst bleach/_vendor/README.rst tests_website/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.3.1-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov 3.3.1-1
- Update to 3.3.1

* Wed Sep 08 2021 Evgeni Golov - 3.3.0-2
- Build against Python 3.8

* Mon Feb 22 2021 Evgeni Golov - 3.3.0-1
- Release python-bleach 3.3.0

* Mon Sep 28 2020 Evgeni Golov 3.2.1-1
- Update to 3.2.1

* Tue Jun 23 2020 Evgeni Golov - 3.1.5-1
- Initial package.
