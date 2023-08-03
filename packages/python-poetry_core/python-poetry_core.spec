%{?python_disable_dependency_generator}
%global pypi_name poetry_core

Name:           python-%{pypi_name}
Version:        1.6.1
Release:        1%{?dist}
Summary:        Poetry PEP 517 Build Backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-poetry/poetry-core
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip

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
%{python3_sitelib}/poetry/core/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Thu Aug 03 2023 Odilon Sousa <osousa@redhat.com> - 1.6.1-1
- Release python-poetry_core 1.6.1

* Mon Jul 24 2023 Odilon Sousa - 1.4.0-1
- Initial package.