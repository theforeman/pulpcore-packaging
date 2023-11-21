%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name requests
%{?python_disable_dependency_generator}

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.31.0
Release:        3%{?dist}
Summary:        Python HTTP for Humans

License:        Apache 2.0
URL:            https://requests.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-certifi >= 2017.4.17
Requires:       %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer >= 2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 1.3.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna < 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyOpenSSL >= 0.14
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.21.1

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
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.31.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.31.0-2
- Build against python 3.11

* Mon Jul 03 2023 Patrick Creech <pcreech@redhat.com> - 2.31.0-1
- Release python-requests 2.31.0

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.28.1-1
- Release python-requests 2.28.1

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 2.27.1-3
- Adding the macro python_disable_dependency_generator to avoid auto dependency

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.27.1-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.27.1-1
- Release python-requests 2.27.1

* Wed Nov 17 2021 Evgeni Golov - 2.26.0-3
- Use charset-normalizer instead of chardet

* Tue Nov 16 2021 Evgeni Golov - 2.26.0-2
- Allow idna 4, 2.26 supports it

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.26.0-1
- Release python-requests 2.26.0

* Mon Sep 06 2021 Evgeni Golov - 2.25.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.25.1-1
- Update to 2.25.1

* Mon Jul 20 2020 Evgeni Golov 2.24.0-1
- Update to 2.24.0

* Wed Mar 18 2020 Samir Jha 2.23.0-1
- Update to 2.23.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.22.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.22.0-1
- Initial package.
