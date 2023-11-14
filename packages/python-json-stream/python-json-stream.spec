%{?python_disable_dependency_generator}
%global debug_package %{nil}

%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11
%global pypi_name json-stream
%global pkg_name json_stream

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        1
Summary:        Streaming JSON encoder and decoder

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/daggaz/json-stream
Source:         https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  pyproject-rpm-macros

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}
Requires:       python%{python3_pkgversion}-json_stream_rs_tokenizer >= 0.4.17

%description -n python%{python3_pkgversion}-%{pkg_name}
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

%files -n python%{python3_pkgversion}-%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/
%{python3_sitelib}/%{pkg_name}/

%changelog
* Mon Nov 13 2023 Odilon Sousa <osousa@redhat.com> - 2.3.2-1
- Initial package.