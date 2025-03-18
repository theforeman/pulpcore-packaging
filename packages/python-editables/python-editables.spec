%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name editables 

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.5
Release:        2%{?dist}
Summary:        Editable installations

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/editables/
Source:         https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 0.5-2
- Rebuild against python3.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.5-1
- Update to 0.5

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa - 0.4-1
- Initial package.