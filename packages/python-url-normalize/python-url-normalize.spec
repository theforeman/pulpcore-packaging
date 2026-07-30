%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name url-normalize
%global src_name url_normalize

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.2.1
Release:        2%{?dist}
Summary:        URL normalization for Python

License:        MIT
URL:            https://github.com/niksite/url-normalize
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-idna

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
%doc README.md
%{_bindir}/url-normalize
%{python3_sitelib}/url_normalize
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.2.1-2
- Bump release for EL10 rebuild

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.1-1
- Update to 2.2.1
- Fix Source0: tarball uses underscores (url_normalize) since 2.x
- Drop stale Requires: python-six; add Requires: python-idna (new dep in 2.x)
- Switch to pyproject build (setup.py removed in 2.x)
- Add url-normalize binary to files section

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 1.4.3-9
- Rebuild against python3.12

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
