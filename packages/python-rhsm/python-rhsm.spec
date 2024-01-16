%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name rhsm

Name:           python-%{pypi_name}
Version:        1.19.2
Release:        7%{?dist}
Summary:        A Python library to communicate with a Red Hat Unified Entitlement Platform

License:        GPLv2
URL:            http://fedorahosted.org/candlepin
Source0:        %{pypi_source}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildRequires:  openssl-devel

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-iniparse
Requires:       python%{python3_pkgversion}-dateutil

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}



%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
PYTHON_RHSM_VERSION=%{version} PYTHON_RHSM_RELEASE=%{release} %py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.19.2-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.19.2-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.19.2-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.19.2-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.19.2-3
- Build against python 3.9

* Thu Nov 04 2021 Justin Sherrill <jsherril@redhat.com> 1.19.2-2
- add el8 dateutils requirement

* Thu Oct 14 2021 Evgeni Golov - 1.19.2-1
- Initial package.
