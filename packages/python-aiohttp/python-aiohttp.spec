%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp

Name:           python-%{pypi_name}
Version:        3.9.5
Release:        1%{?dist}
Summary:        Async http client/server framework (asyncio)

License:        Apache 2
URL:            https://github.com/aio-libs/aiohttp
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-brotli
Requires:       python%{python3_pkgversion}-aiodns
Requires:       python%{python3_pkgversion}-aiosignal >= 1.1.2
Requires:       python%{python3_pkgversion}-attrs >= 17.3.0
Requires:       python%{python3_pkgversion}-charset-normalizer < 3.0
Requires:       python%{python3_pkgversion}-charset-normalizer >= 2.0
Requires:       python%{python3_pkgversion}-frozenlist >= 1.1.1
Requires:       python%{python3_pkgversion}-multidict < 7.0
Requires:       python%{python3_pkgversion}-multidict >= 4.5
Requires:       python%{python3_pkgversion}-yarl < 2.0
Requires:       python%{python3_pkgversion}-yarl >= 1.0

# aiohttp depends on stdlib's mimetypes which reads /etc/mime.types
Requires:       /etc/mime.types


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt vendor/llhttp/LICENSE-MIT
%doc README.rst vendor/llhttp/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.9.5-1
- Update to 3.9.5

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 3.9.4-1
- Release python-aiohttp 3.9.4

* Fri Mar 01 2024 Odilon Sousa <osousa@redhat.com> - 3.9.2-1
- Release python-aiohttp 3.9.2

* Tue Jan 30 2024 Odilon Sousa <osousa@redhat.com> - 3.9.1-1
- Release python-aiohttp 3.9.1

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 3.8.6-1
- Release python-aiohttp 3.8.6

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.8.3-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.8.3-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.8.3-5
- Add python39 obsoletes to package

* Mon Nov 13 2023 Odilon Sousa <osousa@redhat.com> - 3.8.3-4
- Remove cchardet since it's only request for Python < 3.10

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.8.3-3
- Build against python 3.11

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.8.3-2
- Remove asynctest requirement, only required for python <3.8

* Fri Feb 03 2023 Odilon Sousa 3.8.3-1
- Update to 3.8.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.8.1-3
- Build against python 3.9

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 3.8.1-2
- Fixup runtime dependencies

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.8.1-1
- Release python-aiohttp 3.8.1

* Wed Sep 29 2021 Brian Bouterse <bmbouter@redhat.com> 3.7.4-4
- Adds patch to enable secure proxy support

* Mon Sep 27 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.4-3
- Depend on /etc/mime.types

* Mon Sep 06 2021 Evgeni Golov - 3.7.4-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.7.4-1
- Update to 3.7.4

* Thu Oct 29 2020 Evgeni Golov 3.7.2-1
- Update to 3.7.2

* Tue Apr 14 2020 Justin Sherrill <jsherril@redhat.com> 3.6.2-4
- fixing patch application

* Mon Apr 13 2020 Brian Bouterse <bmbouter@redhat.com> - 3.6.2-3
- Raised incoming http header size limits that aiohttp Server accepts

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.6.2-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.6.2-1
- Initial package.
