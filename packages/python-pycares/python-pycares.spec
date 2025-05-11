%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pycares

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.8.0
Release:        1%{?dist}
Summary:        Python interface for c-ares

License:        MIT
URL:            http://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.5.0
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-cffi >= 1.5.0
Requires:       python%{python3_pkgversion}-idna >= 2.1

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
%license LICENSE deps/c-ares/LICENSE.md
%doc PYPIREADME.rst README.rst deps/c-ares/README.md deps/c-ares/README.msvc deps/c-ares/test/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun May 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.8.0-1
- Update to 4.8.0

* Wed Apr 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.6.1-1
- Update to 4.6.1

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 4.5.0-2
- Rebuild against python3.12

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.5.0-1
- Update to 4.5.0

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.4.0-1
- Update to 4.4.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.1.2-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.1.2-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.1.2-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.1.2-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.1.2-2
- Build against python 3.9

* Wed Nov 03 2021 Odilon Sousa 4.1.2-1
- Update to 4.1.2

* Wed Sep 08 2021 Evgeni Golov - 4.0.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 4.0.0-1
- Update to 4.0.0

* Thu Nov 05 2020 Evgeni Golov - 3.1.1-2
- Fix License tag in spec file

* Wed Mar 18 2020 Samir Jha - 3.1.1-1
- Initial package.
