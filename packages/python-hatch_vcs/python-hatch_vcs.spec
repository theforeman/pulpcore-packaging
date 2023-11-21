%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name hatch_vcs 
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        4%{?dist}
Summary:        Hatch plugin for versioning with your preferred VCS

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/hatch-vcs/
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:  python%{python3_pkgversion}-hatchling
Requires:  python%{python3_pkgversion}-setuptools-scm
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

%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.3.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.3.0-3
- Build against python 3.11

* Wed Sep 13 2023 Odilon Sousa <osousa@redhat.com> - 0.3.0-2
- Disable dependency generator for hatch_vcs

* Wed Jul 19 2023 Odilon Sousa - 0.3.0-1
- Initial package.
