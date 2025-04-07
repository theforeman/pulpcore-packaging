%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name CacheControl
%global srcname cachecontrol

Name:           python%{python3_pkgversion}-%{srcname}
Version:        0.14.2
Release:        5%{?dist}
Summary:        httplib2 caching for requests

License:        None
URL:            https://github.com/ionrock/cachecontrol
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

Requires:       python%{python3_pkgversion}-msgpack >= 0.5.2
Requires:       python%{python3_pkgversion}-msgpack < 2.0.0
Requires:       python%{python3_pkgversion}-requests  >= 2.16.0
Requires:       python%{python3_pkgversion}-filelock >= 3.8.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

Obsoletes:      python3.11-%{srcname} < %{version}-%{release}

%description
%{summary}


%package -n python%{python3_pkgversion}-%{srcname}+filecache
Summary: Metapackage for python3-cachecontrol: filecache extra
Requires: python%{python3_pkgversion}-filelock >= 3.8.0

%description -n python%{python3_pkgversion}-%{srcname}+filecache
This is a metapackage bringing in filecache extra requires for python%{python3_pkgversion}-%{srcname}
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{srcname}+filecache
%ghost %{python3_sitelib}/%{srcname}-%{version}.dist-info/

%prep
set -ex
%autosetup -n %{srcname}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%exclude %{_bindir}/doesitcache


%changelog
* Mon Apr 07 2025 Odilon Sousa <osousa@redhat.com> - 0.14.2-5
- Add obsoletes for python3.11 package

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 0.14.2-4
- Drop python-filelock dependancy

* Fri Mar 21 2025 Odilon Sousa <osousa@redhat.com> - 0.14.2-3
- Rebuild against python3.12

* Wed Feb 19 2025 Odilon Sousa <osousa@redhat.com> - 0.14.2-2
- Add filecache metapackage to cachecontrol

* Tue Feb 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.14.2-1
- Update to 0.14.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.12.14-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.12.14-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.12.14-2
- Build against python 3.11

* Fri Aug 04 2023 Odilon Sousa <osousa@redhat.com> - 0.12.14-1
- Initial package.
