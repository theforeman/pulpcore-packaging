%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}

%global pypi_name flit

Name:           python-%{pypi_name}
Version:        3.9.0
Release:        6%{?dist}
Summary:        Distribution-building parts of Flit. See flit package for more information

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://pypi.org/project/flit-core/
Source:         https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-tomli_w
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-flit_core
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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/flit

%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.9.0-6
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.9.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-4
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-3
- Fix tomli_w requirement

* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-2
- Add package requirements

* Fri Jul 14 2023 Odilon Sousa - 3.9.0-1
- Initial package.
