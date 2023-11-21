%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name keyring

Name:           python-%{pypi_name}
Version:        24.2.0
Release:        3%{?dist}
Summary:        Store and access your passwords safely.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/keyring
Source:         https://files.pythonhosted.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-jaraco.classes
Requires:       python%{python3_pkgversion}-SecretStorage
Requires:       python%{python3_pkgversion}-jeepney
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
# rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 24.2.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 24.2.0-2
- Build against python 3.11

* Fri Jul 21 2023 Odilon Sousa - 24.2.0-1
- Initial package.