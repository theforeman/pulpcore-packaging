%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name jaraco.classes
%global package_name jaraco-classes

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        Utility functions for Python class constructs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
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
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sun Jun 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 3.2.3-5
- Rebuild against python3.12

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.2.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.2.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.2.3-2
- Build against python 3.11

* Wed Jul 19 2023 Odilon Sousa - 3.2.3-1
- Initial package.