%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name markdown-it-py
%global src_name markdown_it_py

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Python port of markdown-it. Markdown parsing, done right!

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py/
Source:         https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

Requires:  python%{python3_pkgversion}-mdurl

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
%{python3_sitelib}/markdown_it
%exclude %{_bindir}/markdown-it
%{python3_sitelib}/%{src_name}-%{version}.dist-info/

%changelog
* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 2.2.0-1
- Initial package.