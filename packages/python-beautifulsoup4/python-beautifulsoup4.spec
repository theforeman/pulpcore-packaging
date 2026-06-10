%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name beautifulsoup4

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.15.0
Release:        1%{?dist}
Summary:        Screen-scraping library

License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:       python%{python3_pkgversion}-soupsieve > 1.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/bs4
%{python3_sitelib}/bs4/builder
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.15.0-1
- Update to 4.15.0

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.14.3-1
- Update to 4.14.3
- Drop bs4/tests from %files (no longer installed by upstream since 4.14.x)

* Wed Apr 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.13.4-1
- Update to 4.13.4

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 4.13.3-2
- Rebuild against python3.12

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.13.3-1
- Update to 4.13.3

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.12.3-1
- Update to 4.12.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.11.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.11.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.11.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.11.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 4.11.2-1
- Update to 4.11.2

* Tue Sep 20 2022 Odilon Sousa 4.11.1-1
- Update to 4.11.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.10.0-2
- Build against python 3.9

* Mon Feb 21 2022 Odilon Sousa <osousa@redhat.com> - 4.10.0-1
- Initial package.
