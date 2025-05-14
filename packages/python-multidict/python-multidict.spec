%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name multidict

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        6.4.3
Release:        1%{?dist}
Summary:        multidict implementation

License:        Apache 2
URL:            https://github.com/aio-libs/multidict
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

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
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed May 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.4.3-1
- Update to 6.4.3

* Sun May 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.2.0-1
- Update to 6.2.0

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 6.1.0-2
- Rebuild against python3.12

* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.0-1
- Update to 6.1.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 6.0.4-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 6.0.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 6.0.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.0.4-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 6.0.4-1
- Update to 6.0.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 6.0.2-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa 6.0.2-1
- Update to 6.0.2

* Wed Nov 03 2021 Odilon Sousa 5.2.0-1
- Update to 5.2.0

* Mon Sep 06 2021 Evgeni Golov - 5.1.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 5.1.0-1
- Update to 5.1.0

* Thu Oct 29 2020 Evgeni Golov 5.0.0-1
- Update to 5.0.0

* Thu Jun 04 2020 Evgeni Golov 4.7.6-1
- Update to 4.7.6

* Wed Mar 18 2020 Samir Jha 4.7.5-1
- Update to 4.7.5

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.7.4-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 4.7.4-1
- Update to 4.7.4

* Mon Jan 06 2020 Evgeni Golov 4.7.3-1
- Update to 4.7.3

* Fri Dec 13 2019 Evgeni Golov 4.7.1-1
- Update to 4.7.1

* Mon Nov 18 2019 Evgeni Golov - 4.5.2-1
- Initial package.
