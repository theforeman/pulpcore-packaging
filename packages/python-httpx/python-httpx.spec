%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name httpx 

Name:           python-%{pypi_name}
Version:        0.24.1
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

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-certifi
Requires:       python%{python3_pkgversion}-httpcore >= 0.15.0
Requires:       python%{python3_pkgversion}-httpcore < 0.18.0
Requires:       python%{python3_pkgversion}-idna
Requires:       python%{python3_pkgversion}-sniffio
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
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
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.24.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.24.1-2
- Build against python 3.11

* Wed Jul 26 2023 Odilon Sousa - 0.24.1-1
- Initial package.
