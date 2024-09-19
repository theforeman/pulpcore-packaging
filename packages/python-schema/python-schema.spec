%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name schema

Name:           python-%{pypi_name}
Version:        0.7.7
Release:        1%{?dist}
Summary:        Simple data validation library

License:        MIT
URL:            https://github.com/keleshev/schema
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
${summary}


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
%license LICENSE-MIT
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.7-1
- Update to 0.7.7

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.7.5-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.7.5-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.7.5-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.7.5-3
- Build against python 3.11

* Fri May 27 2022 Odilon Sousa <osousa@redhat.com> - 0.7.5-2
- Bump release to rebuild against python39

* Thu May 26 2022 Odilon Sousa - 0.7.5-1
- Release python-schema 0.7.5

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.7.4-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.7.4-2
- Build against Python 3.8

* Wed Aug 11 2021 Evgeni Golov - 0.7.4-1
- Initial package.

