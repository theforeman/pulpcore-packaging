%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name drf-yasg

Name:           python-%{pypi_name}
Version:        1.17.1
Release:        7%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code

License:        BSD License
URL:            https://github.com/axnsan12/drf-yasg
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-coreapi >= 2.3.3
Requires:       python%{python3_pkgversion}-coreschema >= 0.0.4
Requires:       python%{python3_pkgversion}-inflection >= 0.3.1
Requires:       python%{python3_pkgversion}-django >= 1.11.7	
Requires:       python%{python3_pkgversion}-django-rest-framework >= 3.8
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-ruamel-yaml >= 0.15.34
Requires:       python%{python3_pkgversion}-six >= 1.10.0
Requires:       python%{python3_pkgversion}-uritemplate >= 3.0.0


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
%license docs/license.rst LICENSE.rst
%doc docs/readme.rst README.rst
%{python3_sitelib}/drf_yasg
%{python3_sitelib}/drf_yasg-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.17.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.17.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.17.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.17.1-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.17.1-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.17.1-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 1.17.1-1
- Update to 1.17.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.17.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.17.0-1
- Initial package.
