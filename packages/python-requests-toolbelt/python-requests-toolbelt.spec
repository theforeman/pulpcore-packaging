%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.8
%global pypi_name requests-toolbelt

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        A utility belt for advanced users of python-requests

License:        Apache 2.0
URL:            https://toolbelt.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}

%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.0.1


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/requests_toolbelt
%{python3_sitelib}/requests_toolbelt-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-1
- Initial package.
