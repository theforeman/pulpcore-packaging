%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name bandersnatch

Name:           python-%{pypi_name}
Version:        6.1.0
Release:        4%{?dist}
Summary:        Mirroring tool that implements the client (mirror) side of PEP 381

License:        Academic Free License, version 3
URL:            https://github.com/pypa/bandersnatch/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-aiohttp-socks
Requires:       python%{python3_pkgversion}-aiohttp-xmlrpc
Requires:       python%{python3_pkgversion}-filelock
Requires:       python%{python3_pkgversion}-humanfriendly
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
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
%license LICENSE
%doc README.md
%{_bindir}/bandersnatch
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/bandersnatch_filter_plugins
%{python3_sitelib}/bandersnatch_storage_plugins
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 6.1.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 6.1.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.1.0-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa 6.1.0-1
- Update to 6.1.0

* Tue Sep 20 2022 Odilon Sousa 5.3.0-1
- Update to 5.3.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 5.1.1-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.1.1-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 5.1.1-1
- Release python-bandersnatch 5.1.1

* Tue Oct 26 2021 Evgeni Golov - 4.4.0-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 4.4.0-3
- Build against Python 3.8

* Wed Aug 11 2021 Evgeni Golov - 4.4.0-2
- Patch out setuptools version requirement

* Tue Jul 13 2021 Evgeni Golov - 4.4.0-1
- Initial package.
