%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global pkg_name %{name}

# Created by pyp2rpm-3.3.3
%global pypi_name pyparsing

Name:           python-%{pypi_name}
Version:        2.4.7
Release:        4%{?dist}
Summary:        Python parsing module

License:        MIT License
URL:            https://github.com/pyparsing/pyparsing/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install

set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst examples/0README.html
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 10 2023 Odilon Sousa <osousa@redhat.com> - 2.4.7-4
- Rebuild against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.4.7-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 2.4.7-2
- Build against Python 3.8

* Tue Apr 14 2020 Evgeni Golov 2.4.7-1
- Update to 2.4.7

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.6-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.4.6-1
- Update to 2.4.6

* Mon Nov 18 2019 Evgeni Golov - 2.4.5-1
- Initial package.
