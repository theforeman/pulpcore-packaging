%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name chardet

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        5.2.0
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 3

License:        LGPL
URL:            https://github.com/chardet/chardet
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%exclude %{_bindir}/chardetect
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 5.2.0-1
- Release python-chardet 5.2.0

* Tue Sep 20 2022 Odilon Sousa 5.0.0-1
- Update to 5.0.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.0.0-2
- Build against python 3.9

* Sat Feb 05 2022 Odilon Sousa <osousa@redhat.com> - 4.0.0-1
- Release python-chardet 4.0.0

* Mon Sep 06 2021 Evgeni Golov - 3.0.4-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.0.4-1
- Initial package.
