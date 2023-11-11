%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name build

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        2%{?dist}
Summary:        A simple, correct Python build frontend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/build
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core
%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-packaging >= 19.0
Requires:       python%{python3_pkgversion}-pyproject_hooks
Requires:       python%{python3_pkgversion}-importlib-metadata >= 4.6
Requires:       python%{python3_pkgversion}-tomli >= 1.1.0

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
%{_bindir}/pyproject-build


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.10.0-2
- Build against python 3.11

* Thu Aug 03 2023 Odilon Sousa - 0.10.0-1
- Initial package.