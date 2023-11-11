%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name jeepney 

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        2%{?dist}
Summary:        This is the extensible, standards compliant build backend used by Hatch.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/tree/master/backend
Source:         https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

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
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.8.0-2
- Build against python 3.11

* Wed Jul 19 2023 Odilon Sousa - 0.8.0-1
- Initial package.
