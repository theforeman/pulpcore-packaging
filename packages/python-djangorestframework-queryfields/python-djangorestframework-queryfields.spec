%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework-queryfields

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Serialize a partial subset of fields in the API

License:        MIT
URL:            https://github.com/wimglenn/djangorestframework-queryfields
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%doc README.rst
%{python3_sitelib}/drf_queryfields
%{python3_sitelib}/djangorestframework_queryfields-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.0-1
- Update to 1.1.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.0-8
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.0-7
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-6
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.0-5
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.0-4
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.0.0-3
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.0.0-1
- Initial package.
