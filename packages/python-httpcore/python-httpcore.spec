%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name httpcore

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        2%{?dist}
Summary:        A minimal low-level HTTP client

License:        BSD
URL:            https://github.com/encode/httpcore
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

Requires:       python%{python3_pkgversion}-anyio
Requires:       python%{python3_pkgversion}-certifi
Requires:       python%{python3_pkgversion}-h11
Requires:       python%{python3_pkgversion}-sniffio

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
* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 1.0.7-1
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.7-1
- Update to 1.0.7

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.17.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.17.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.17.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.17.3-2
- Build against python 3.11

* Fri Jul 21 2023 Odilon Sousa <osousa@redhat.com> - 0.17.3-1
- Initial package.
