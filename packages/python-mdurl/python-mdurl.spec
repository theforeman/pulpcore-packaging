%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name mdurl

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Markdown URL utilities

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/mdurl/
Source:         https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

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
* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 0.1.2-2
- Drop flit_core as requirement

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 0.1.2-1
- Initial package.
