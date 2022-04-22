%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Parsley
%global srcname parsley

Name:           %{?scl_prefix}python-%{srcname}
Version:        1.3
Release:        2%{?dist}
Summary:        Parsing and pattern matching made easy

License:        MIT License
URL:            http://launchpad.net/parsley
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Provides:       %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name} = %{version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc terml/README.txt
%{python3_sitelib}/__pycache__/parsley.*
%{python3_sitelib}/parsley.py
%{python3_sitelib}/ometa
%{python3_sitelib}/terml
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.3-2
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov - 1.3-1
- Initial package.
