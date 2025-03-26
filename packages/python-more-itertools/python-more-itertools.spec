%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name more-itertools

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        10.6.0
Release:        2%{?dist}
Summary:        This is the extensible, standards compliant build backend used by Hatch.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/tree/master/backend
Source:         https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  python%{python3_pkgversion}-pip
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
%{python3_sitelib}/more_itertools
%{python3_sitelib}/more_itertools-%{version}.dist-info/

%changelog
* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 10.6.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 10.6.0-1
- Update to 10.6.0

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 9.1.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 9.1.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 9.1.0-2
- Build against python 3.11

* Wed Jul 19 2023 Odilon Sousa - 9.1.0-1
- Initial package.
