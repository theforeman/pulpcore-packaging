%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name poetry_plugin_export

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.8.0
Release:        2%{?dist}
Summary:        Poetry plugin to export the dependencies to various formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-poetry/poetry-plugin-export
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core >= %{version}

Requires:       python%{python3_pkgversion}-poetry >= 1.7
Requires:       python%{python3_pkgversion}-poetry < 3.0
Requires:       python%{python3_pkgversion}-poetry_core >= 1.8
Requires:       python%{python3_pkgversion}-poetry_core < 3.0.0

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
* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com>
- Rebuild against python3.12

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.0-1
- Update to 1.8.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.4.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.4.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.4.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.4.0-2
- Build against python 3.11

* Thu Aug 03 2023 Odilon Sousa - 1.4.0-1
- Initial package.