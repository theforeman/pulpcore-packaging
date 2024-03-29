%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name url-normalize

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        8%{?dist}
Summary:        URL normalization for Python

License:        MIT
URL:            https://github.com/niksite/url-normalize
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-six


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/url_normalize
%{python3_sitelib}/url_normalize-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.4.3-8
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.4.3-7
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.4.3-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.4.3-5
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.4.3-4
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.4.3-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.4.3-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 1.4.3-1
- Update to 1.4.3

* Tue Aug 25 2020 Evgeni Golov - 1.4.2-1
- Initial package.
