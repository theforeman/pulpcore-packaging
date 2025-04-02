%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pypi-simple
%global src_name pypi_simple

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.6.1
Release:        1%{?dist}
Summary:        PyPI Simple Repository API client library

License:        MIT
URL:            https://github.com/jwodder/pypi-simple
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:  python%{python3_pkgversion}-packaging
Requires:  python%{python3_pkgversion}-requests
Requires:  python%{python3_pkgversion}-beautifulsoup4
Requires:  python%{python3_pkgversion}-pydantic
Requires:  python%{python3_pkgversion}-mailbits >= 0.2

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
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Wed Apr 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.6.1-1
- Update to 1.6.1

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 0.10.0-2
- Rebuild against python3.12

* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.0-1
- Update to 0.10.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.9.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.9.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.9.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.9.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.9.0-2
- Build against python 3.9

* Tue Feb 22 2022 Evgeni Golov - 0.9.0-1
- Initial package.
