%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.8
%global pypi_name pyasn1-modules

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.2.8
Release:        1%{?dist}
Summary:        A collection of ASN.1-based protocols modules

License:        BSD-2-Clause
URL:            https://github.com/etingof/pyasn1-modules
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyasn1 >= 0.4.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyasn1 >= 0.4.6
Conflicts:       %{?scl_prefix}python%{python3_pkgversion}-pyasn1 > 0.6

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
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/pyasn1_modules
%{python3_sitelib}/pyasn1_modules-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Aug 25 2022 Odilon Sousa <osousa@redhat.com> - 0.2.8-1
- Initial package.
