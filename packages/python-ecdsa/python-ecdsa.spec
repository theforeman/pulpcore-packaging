%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name ecdsa

Name:           python-%{pypi_name}
Version:        0.18.0
Release:        5%{?dist}
Summary:        ECDSA cryptographic signature library (pure python)

License:        MIT
URL:            http://github.com/tlsfuzzer/python-ecdsa
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.18.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.18.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.18.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.18.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 0.18.0-1
- Update to 0.18.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.14.1-2
- Build against python 3.9

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 0.14.1-1
- Release python-ecdsa 0.14.1

* Mon Sep 06 2021 Evgeni Golov - 0.13.3-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.3-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 0.13.3-1
- Initial package.
