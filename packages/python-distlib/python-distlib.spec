%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name distlib

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Distlib is a library which implements low-level functions that relate to packaging and distribution of Python software.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/distlib
Source:         https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


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
* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.2-1
- Update to 0.4.2

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.0-1
- Update to 0.4.0

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 0.3.9-2
- Rebuild against python3.12

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.9-1
- Update to 0.3.9

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.3.6-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.3.6-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.3.6-2
- Build against python 3.11

* Tue Jul 25 2023 Odilon Sousa - 0.3.6-1
- Initial package.