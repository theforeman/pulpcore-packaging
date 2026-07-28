%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name async-lru
%global src_name async_lru

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.0.5
Release:        2%{?dist}
Summary:        Simple lru_cache for asyncio

License:        MIT
URL:            https://github.com/aio-libs/async_lru
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}

%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/async_lru
%{python3_sitelib}/async_lru-%{version}.dist-info


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 2.0.5-2
- Bump release for EL10 rebuild

* Sun Sep 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.5-1
- Update to 2.0.5
- Migrate to pyproject_wheel build macros

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 2.0.4-2
- Rebuild against python3.12

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.4-1
- Update to 2.0.4

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.3-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 1.0.3-1
- Update to 1.0.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.2-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.2-2
- Build against Python 3.8

* Mon Jan 11 2021 Evgeni Golov - 1.0.2-1
- Initial package.
