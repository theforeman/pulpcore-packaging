%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name typing-inspection
%global srcname typing_inspection

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/pydantic/typing-inspection/
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling

Requires:  python%{python3_pkgversion}-typing-extensions >= 4.12.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
* Sun Jun 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.1-1
- Update to 0.4.1

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 0.4.0-1
- Initial Release

