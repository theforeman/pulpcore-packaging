%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global debug_package %{nil}

# Created by pyp2rpm-3.3.8
%global pypi_name rapidfuzz

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.14.3
Release:        1%{?dist}
Summary:        rapid fuzzy string matching

License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-scikit-build-core
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

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
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.14.3-1
- Update to 3.14.3
- Switch to pyproject build (setup.py removed, migrated to scikit-build-core at 3.10.0)
- Replace scikit-build with scikit-build-core; add cmake, gcc, gcc-c++
- Fix files section to use python3_sitearch and .dist-info (C extension)

* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 3.9.7-1
- Release python-rapidfuzz 3.9.7

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 2.15.1-6
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.15.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.15.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.15.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.15.1-2
- Build against python 3.11

* Fri Aug 04 2023 Odilon Sousa <osousa@redhat.com> - 2.15.1-1
- Initial package.
