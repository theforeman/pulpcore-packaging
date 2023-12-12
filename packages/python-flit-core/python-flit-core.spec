%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global pypi_name flit_core

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.9.0
Release:        6%{?dist}
Summary:        Distribution-building parts of Flit. See flit package for more information

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://pypi.org/project/flit-core/
Source:         https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tomli
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip

Provides:       %{pypi_name} = %{version}

%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-tomli
Requires:       pyproject-rpm-macros
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pip


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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.9.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.9.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-4
- Build against python 3.11

* Fri Oct 13 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-3
- Add pyproject-rpm-macros to requirements

* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-2
- Add package requirements

* Fri Jul 14 2023 dilon Sousa - 3.9.0-1
- Initial package.
