%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name async-timeout

Name:           python-%{pypi_name}
Version:        4.0.3
Release:        1%{?dist}
Summary:        Timeout context manager for asyncio programs

License:        Apache 2
URL:            https://github.com/aio-libs/async-timeout
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.6.5


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
%doc README.rst
%{python3_sitelib}/async_timeout
%{python3_sitelib}/async_timeout-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.3-1
- Update to 4.0.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.0.2-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.0.2-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.0.2-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.0.2-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.0.2-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa 4.0.2-1
- Update to 4.0.2

* Mon Sep 06 2021 Evgeni Golov - 3.0.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.0.1-1
- Initial package.
