%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name annotated-types
%global srcname annotated_types

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/annotated-types/annotated-types/
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling


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
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 0.7.0-2
- Bump release for EL10 rebuild

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 0.7.0-1
- Initial Release

