%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

%global pypi_name flit_scm

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.7.0
Release:        4%{?dist}
Summary:        A PEP 518 build backend that uses setuptools_scm to generate a version file from your version control system, then flit_core to build the package.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://gitlab.com/WillDaSilva/flit_scm
Source:         https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tomli
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flit_core
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm

%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm
Requires:       %{?scl_prefix}python%{python3_pkgversion}-tomli
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flit_core
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.7.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-3
- Build against python 3.11

* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-2
- Add package requirements

* Fri Jul 14 2023 Odilon Sousa - 1.7.0-1
- Initial package.
