%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name typing-extensions

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.7.1
Release:        4%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3

License:        PSF
URL:            https://github.com/python/typing/blob/master/typing_extensions/README.rst
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/typing_extensions-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flit_core
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tomli
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n typing_extensions-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/__pycache__/typing_extensions.*
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/typing_extensions-%{version}.dist-info/


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.7.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.7.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.7.1-2
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 4.7.1-1
- Release python-typing-extensions 4.7.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.10.0.2-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.10.0.2-1
- Release python-typing-extensions 3.10.0.2

* Fri Sep 10 2021 Evgeni Golov - 3.7.4.3-3
- Don't require typing, our Python is new enough

* Wed Sep 08 2021 Evgeni Golov - 3.7.4.3-2
- Build against Python 3.8

* Tue Sep 01 2020 Evgeni Golov 3.7.4.3-1
- Update to 3.7.4.3

* Tue Apr 14 2020 Evgeni Golov 3.7.4.2-1
- Update to 3.7.4.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.4.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.7.4.1-1
- Initial package.
