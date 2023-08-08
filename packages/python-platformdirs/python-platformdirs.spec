%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.8
%global pypi_name platformdirs

Name:           python-%{pypi_name}
Version:        3.10.0
Release:        1%{?dist}
Summary:        A small Python module for determining appropriate platform-specific dirs, e

License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}


%package -n    python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
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
* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.10.0-1
- Release python-platformdirs 3.10.0

* Mon Jul 24 2023 Odilon Sousa <osousa@redhat.com> - 2.6.2-1
- Initial package.
