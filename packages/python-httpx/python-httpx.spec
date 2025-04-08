%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name httpx 

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.28.1
Release:        3%{?dist}
Summary:        The next generation HTTP client.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:       python%{python3_pkgversion}-certifi
Requires:       python%{python3_pkgversion}-httpcore >= 1
Requires:       python%{python3_pkgversion}-httpcore < 2
Requires:       python%{python3_pkgversion}-idna
Requires:       python%{python3_pkgversion}-sniffio

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.28.1-3
- Add obsoletes for python3.11 package

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 0.28.1-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.28.1-1
- Update to 0.28.1

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.24.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.24.1-2
- Build against python 3.11

* Wed Jul 26 2023 Odilon Sousa - 0.24.1-1
- Initial package.
