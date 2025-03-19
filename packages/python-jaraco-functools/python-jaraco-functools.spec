%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name jaraco_functools
%global package_name jaraco-functools

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.1.0
Release:        2%{?dist}
Summary:        Additional functools in the spirit of stdlib's functools.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/jaraco.functools
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-more-itertools

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
# rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/jaraco
%{python3_sitelib}/jaraco.functools-%{version}.dist-info/


%changelog
* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 4.1.0-2
- Rebuild against python3.12

* Wed Jul 19 2023 Odilon Sousa - 4.1.0-1
- Initial package.