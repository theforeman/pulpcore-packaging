%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name editables 

Name:           python-%{pypi_name}
Version:        0.4
Release:        3%{?dist}
Summary:        Editable installations

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/editables/
Source:         https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  pyproject-rpm-macros



%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


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
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa - 0.4-1
- Initial package.