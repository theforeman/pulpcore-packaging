%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name pyproject-metadata
%global pkg_name pyproject_metadata

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.9.0
Release:        2%{?dist}
Summary:        Dataclass for PEP 621 metadata with support for core metadata generation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/pyproject-metadata
Source:         https://files.pythonhosted.org/packages/source/p/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

Requires:  python%{python3_pkgversion}-packaging

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}

%prep
set -ex
%autosetup -n %{pkg_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/

%changelog
* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 0.9.0-2
- Rebuild against python3.12

* Tue Jan 14 2025 Odilon Sousa - 0.9.0-1
- Initial package.
