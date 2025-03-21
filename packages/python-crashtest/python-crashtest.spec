%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name crashtest

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.1
Release:        6%{?dist}
Summary:        Manage Python errors with ease

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sdispater/crashtest
Source:         https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Mar 21 2025 Odilon Sousa <osousa@redhat.com> - 0.4.1-6
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.4.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.4.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.1-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa - 0.4.1-1
- Initial package.