%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name uuid6

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2025.0.1
Release:        2%{?dist}
Summary:        New time-based UUID formats which are suited for use as a database key

License:        MIT
URL:            https://github.com/oittaa/uuid6-python
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}



%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2025.0.1-2
- Bump release for EL10 rebuild

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2025.0.1-1
- Update to 2025.0.1
- Switch to pyproject build (setup.py removed upstream); add setuptools-scm
- Pass SETUPTOOLS_SCM_PRETEND_VERSION to avoid missing git repo in mock
- Fix License tag: None -> MIT
- Fix files section: use .dist-info instead of .egg-info

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 2024.7.10-2
- Rebuild against python3.12

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2024.7.10-1
- Update to 2024.7.10

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2024.1.12-1
- Update to 2024.1.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2023.5.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2023.5.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2023.5.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2023.5.2-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa - 2023.5.2-1
- Initial package.
