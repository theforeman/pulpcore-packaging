%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pydantic

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.11.1
Release:        1%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/pydantic/pydantic/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme >= 22.5.0

Requires:  python%{python3_pkgversion}-typing-extensions >= 4.12.2
Requires:  python%{python3_pkgversion}-annotated-types >= 0.6.0
Requires:  python%{python3_pkgversion}-pydantic-core == 2.33.1
Requires:  python%{python3_pkgversion}-typing-inspection >= 0.4.0

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
* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.11.1-1
- Initial Release

