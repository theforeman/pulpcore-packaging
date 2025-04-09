%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name userpath

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.9.2
Release:        3%{?dist}
Summary:        Cross-platform tool for adding locations to the user PATH, no elevated privileges required!

License:        MIT OR Apache-2.0
URL:            https://github.com/ofek/userpath
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:       python%{python3_pkgversion}-click

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
%{_bindir}/userpath
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 1.9.2-3
- Add obsoletes for python3.11 package

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 1.9.2-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.9.2-1
- Update to 1.9.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.7.0-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.7.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-2
- Build against python 3.11

* Mon Jul 24 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-1
- Initial package.
