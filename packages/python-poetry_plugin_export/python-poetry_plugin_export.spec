%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name poetry_plugin_export

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        3%{?dist}
Summary:        Poetry plugin to export the dependencies to various formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-poetry/poetry-plugin-export
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-poetry_core

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-poetry >= 1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-poetry < 2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-poetry_core >= 1.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-poetry_core < 2.0
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
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.4.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.4.0-2
- Build against python 3.11

* Thu Aug 03 2023 Odilon Sousa - 1.4.0-1
- Initial package.