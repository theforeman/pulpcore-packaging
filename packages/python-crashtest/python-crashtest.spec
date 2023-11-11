%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
%global pypi_name crashtest

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Manage Python errors with ease

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sdispater/crashtest
Source:         https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-poetry_core

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.1-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa - 0.4.1-1
- Initial package.