%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global pkg_name %{name}

# Created by pyp2rpm-3.3.3
%global pypi_name packaging

Name:           python-%{pypi_name}
Version:        21.3
Release:        2%{?dist}
Summary:        Core utilities for Python packages

License:        BSD-2-Clause or Apache-2.0
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyparsing < 3
Requires:       python%{python3_pkgversion}-pyparsing >= 2.0.2
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
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 10 2023 Odilon Sousa <osousa@redhat.com> - 21.3-2
- Rebuild against python 3.11

* Thu Jun 30 2022 Ian Ballou <ianballou67@gmail.com> - 21.3-1
- Bump up to 21.3 for pulp-python

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 21.2-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 21.2-1
- Update to 21.2

* Wed Sep 08 2021 Evgeni Golov - 21.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 21.0-1
- Update to 21.0

* Fri Mar 19 2021 Evgeni Golov 20.9-1
- Update to 20.9

* Thu Jun 04 2020 Evgeni Golov 20.4-1
- Update to 20.4

* Wed Mar 18 2020 Samir Jha 20.3-1
- Update to 20.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.1-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 20.1-1
- Update to 20.1

* Mon Jan 06 2020 Evgeni Golov 20.0-1
- Update to 20.0

* Mon Nov 18 2019 Evgeni Golov - 19.2-1
- Initial package.
