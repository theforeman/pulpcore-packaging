%global pypi_name more-itertools

Name:           python-%{pypi_name}
Version:        9.1.0
Release:        1%{?dist}
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

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
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
%{python3_sitelib}/more_itertools
%{python3_sitelib}/more_itertools-%{version}.dist-info/

%changelog
* Wed Jul 19 2023 Odilon Sousa - 9.1.0-1
- Initial package.
