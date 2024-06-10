%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name gunicorn

Name:           python-%{pypi_name}
Version:        22.0.0
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        MIT
URL:            https://gunicorn.org
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-packaging

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc docs/README.rst README.rst
%{_bindir}/gunicorn
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 22.0.0-1
- Release python-gunicorn 22.0.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 20.1.0-8
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 20.1.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 20.1.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 20.1.0-1
- Update to 20.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.0.4-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 20.0.4-1
- Update to 20.0.4

* Mon Nov 18 2019 Evgeni Golov - 20.0.0-1
- Initial package.
