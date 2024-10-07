%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name requests

Name:           python-%{pypi_name}
Version:        2.32.3
Release:        2%{?dist}
Summary:        Python HTTP for Humans

License:        Apache 2.0
URL:            https://requests.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-certifi >= 2017.4.17
Requires:       python%{python3_pkgversion}-charset-normalizer < 4
Requires:       python%{python3_pkgversion}-charset-normalizer >= 2
Requires:       python%{python3_pkgversion}-idna < 4
Requires:       python%{python3_pkgversion}-idna >= 2.5
Requires:       python%{python3_pkgversion}-pyOpenSSL >= 0.14
Requires:       python%{python3_pkgversion}-urllib3 < 3
Requires:       python%{python3_pkgversion}-urllib3 >= 1.21.1


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Oct 07 2024 Odilon Sousa <osousa@redhat.com> - 2.32.3-2
- Rebuild package using PEP-517 macros

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.32.3-1
- Update to 2.32.3

* Thu Sep 12 2024 Odilon Sousa <osousa@redhat.com> - 2.31.0-6
- Update charset-normalizer requirements for requests3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.31.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.31.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.31.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.31.0-2
- Build against python 3.11

* Mon Jul 03 2023 Patrick Creech <pcreech@redhat.com> - 2.31.0-1
- Release python-requests 2.31.0

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.28.1-1
- Release python-requests 2.28.1

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 2.27.1-3
- Adding the macro python_disable_dependency_generator to avoid auto dependency

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.27.1-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.27.1-1
- Release python-requests 2.27.1

* Wed Nov 17 2021 Evgeni Golov - 2.26.0-3
- Use charset-normalizer instead of chardet

* Tue Nov 16 2021 Evgeni Golov - 2.26.0-2
- Allow idna 4, 2.26 supports it

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.26.0-1
- Release python-requests 2.26.0

* Mon Sep 06 2021 Evgeni Golov - 2.25.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.25.1-1
- Update to 2.25.1

* Mon Jul 20 2020 Evgeni Golov 2.24.0-1
- Update to 2.24.0

* Wed Mar 18 2020 Samir Jha 2.23.0-1
- Update to 2.23.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.22.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.22.0-1
- Initial package.
