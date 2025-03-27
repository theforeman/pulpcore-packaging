%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name anyio

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.8.0
Release:        2%{?dist}
Summary:        High level compatibility layer for multiple asynchronous event loop implementations

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/anyio/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-idna >= 2.8
Requires:       python%{python3_pkgversion}-sniffio >= 1.1
Requires:       python%{python3_pkgversion}-typing-extensions >= 4.5

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Mar 27 2025 Odilon Sousa <osousa@redhat.com> - 4.8.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.8.0-1
- Update to 4.8.0

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.6.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.6.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.6.2-2
- Build against python 3.11

* Fri Jul 21 2023 Odilon Sousa - 3.6.2-1
- Initial package.