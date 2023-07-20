%{?python_disable_dependency_generator}
%global pypi_name hatchling 

Name:           python-%{pypi_name}
Version:        1.18.0
Release:        2%{?dist}
Summary:        This is the extensible, standards compliant build backend used by Hatch.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/tree/master/backend
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pathspec
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-editables
BuildRequires:  python%{python3_pkgversion}-pluggy
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-trove-classifiers
BuildRequires:  pyproject-rpm-macros

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pathspec
Requires:       python%{python3_pkgversion}-editables
Requires:       python%{python3_pkgversion}-pluggy
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-trove-classifiers
Requires:       pyproject-rpm-macros

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
%{_bindir}/%{pypi_name}

%changelog
* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 1.18.0-2
- Add package requirements

* Mon Jul 17 2023 Odilon Sousa - 1.18.0-1
- Initial package.
