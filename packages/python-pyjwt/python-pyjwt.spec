%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name PyJWT
%global srcname pyjwt

Name:           python-%{srcname}
Version:        2.8.0
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python

License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-jwt = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-jwt < %{version}-%{release}
Requires:       python%{python3_pkgversion}-cryptography >= 3.4.0
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
%license LICENSE
%doc README.rst
%exclude %{_bindir}/pyjwt
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.0-1
- Update to 2.8.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.5.0-5
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.5.0-3
- Build against python 3.11

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.5.0-2
- Adding new dependency for python-pyjwt

* Tue Sep 20 2022 Odilon Sousa 2.5.0-1
- Update to 2.5.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.7.1-8
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 1.7.1-7
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 1.7.1-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 22 2021 Evgeni Golov - 1.7.1-5
- Correct provides for Python 3.8

* Mon Sep 06 2021 Evgeni Golov - 1.7.1-4
- Build against Python 3.8

* Thu Aug 27 2020 Evgeni Golov - 1.7.1-3
- Obsolete python3-jwt

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.7.1-1
- Initial package.
