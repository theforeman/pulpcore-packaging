%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name virtualenv
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        20.24.2
Release:        2%{?dist}
Summary:        A tool for creating isolated virtual python environments.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/virtualenv/tree
Source:         https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:  python%{python3_pkgversion}-distlib
Requires:  python%{python3_pkgversion}-filelock
Requires:  python%{python3_pkgversion}-platformdirs

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
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.24.2-2
- Build against python 3.11

* Tue Jul 25 2023 Odilon Sousa - 20.24.2-1
- Initial package.