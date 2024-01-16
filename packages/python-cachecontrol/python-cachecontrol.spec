%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name CacheControl
%global srcname cachecontrol

Name:           python-%{srcname}
Version:        0.12.14
Release:        4%{?dist}
Summary:        httplib2 caching for requests

License:        None
URL:            https://github.com/ionrock/cachecontrol
Source0:        https://files.pythonhosted.org/packages/source/C/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-lockfile >= 0.9
Requires:       python%{python3_pkgversion}-msgpack >= 0.5.2
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-filelock >= 3.8.0
%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{srcname}
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


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{_bindir}/doesitcache
%{python3_sitelib}/cachecontrol
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.12.14-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.12.14-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.12.14-2
- Build against python 3.11

* Fri Aug 04 2023 Odilon Sousa <osousa@redhat.com> - 0.12.14-1
- Initial package.
