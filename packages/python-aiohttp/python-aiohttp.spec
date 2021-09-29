# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp

Name:           python-%{pypi_name}
Version:        3.7.4
Release:        1.1%{?dist}
Summary:        Async http client/server framework (asyncio)

License:        Apache 2
URL:            https://github.com/aio-libs/aiohttp
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-allow-larger-headers.patch
Patch1:         0002-Adds-Secure-Proxy-support.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-async-timeout < 4.0
Requires:       python%{python3_pkgversion}-async-timeout >= 3.0
Requires:       python%{python3_pkgversion}-attrs >= 17.3.0
Requires:       python%{python3_pkgversion}-chardet < 4.0
Requires:       python%{python3_pkgversion}-chardet >= 2.0
Requires:       python%{python3_pkgversion}-idna-ssl >= 1.0
Requires:       python%{python3_pkgversion}-multidict < 7.0
Requires:       python%{python3_pkgversion}-multidict >= 4.5
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.6.5
Requires:       python%{python3_pkgversion}-yarl < 2.0
Requires:       python%{python3_pkgversion}-yarl >= 1.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt vendor/http-parser/LICENSE-MIT
%doc README.rst vendor/http-parser/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 29 2021 Brian Bouterse <bmbouter@redhat.com> 3.7.4-1.1
- Adds patch to enable secure proxy support

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
