%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp-xmlrpc

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.5.0
Release:        8%{?dist}
Summary:        aiohttp XML-RPC server handler and client

License:        MIT
URL:            https://github.com/mosquito/aiohttp-xmlrpc
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-lxml

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
%{python3_sitelib}/aiohttp_xmlrpc
%{python3_sitelib}/aiohttp_xmlrpc-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 1.5.0-8
- Bump release for EL10 rebuild

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 1.5.0-7
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.5.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.5.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.5.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.5.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.5.0-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 1.5.0-1
- Release python-aiohttp-xmlrpc 1.5.0

* Wed Nov 03 2021 Odilon Sousa <osousa@redhat.com> - 1.3.2-1
- Release python-aiohttp-xmlrpc 1.3.2

* Mon Sep 06 2021 Evgeni Golov - 1.3.1-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov - 1.3.1-1
- Initial package.
