%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pathspec

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Utility library for gitignore style pattern matching of file paths

License:        MPL 2.0
URL:            https://github.com/cpburnz/python-pathspec
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools >= 40.8

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Jan 11 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.3-1
- Update to 1.0.3

* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 0.12.1-2
- Rebuild against python3.12

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.12.1-1
- Update to 0.12.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.11.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.11.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.11.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.11.1-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa <osousa@redhat.com> - 0.11.1-1
- Initial package.
