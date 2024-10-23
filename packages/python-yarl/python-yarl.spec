%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name yarl

Name:           python-%{pypi_name}
Version:        1.13.1
Release:        1%{?dist}
Summary:        Yet another URL library

License:        Apache 2
URL:            https://github.com/aio-libs/yarl/
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-idna >= 2.0
Requires:       python%{python3_pkgversion}-multidict >= 4.0
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.7.4


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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.13.1-1
- Update to 1.13.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.8.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.8.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.8.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.8.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.8.2-1
- Update to 1.8.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.7.2-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 1.7.2-1
- Update to 1.7.2

* Wed Sep 08 2021 Evgeni Golov - 1.6.3-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 1.6.3-1
- Update to 1.6.3

* Thu Oct 29 2020 Evgeni Golov 1.6.2-1
- Update to 1.6.2

* Mon Aug 10 2020 Evgeni Golov 1.5.1-1
- Update to 1.5.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Mon Nov 18 2019 Evgeni Golov - 1.3.0-1
- Initial package.
