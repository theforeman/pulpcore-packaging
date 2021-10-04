%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name ansible-builder

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        A tool for building Ansible Execution Environments

License:        Apache-2.0
URL:            https://github.com/ansible/ansible-builder/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pbr
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bindep
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requirements-parser
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif


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
%license LICENSE.md
%doc README.md
%{_bindir}/ansible-builder
%{python3_sitelib}/ansible_builder
%{python3_sitelib}/ansible_builder-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 29 2021 Evgeni Golov - 1.0.1-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Fri Sep 10 2021 Evgeni Golov - 1.0.1-1
- Release python-ansible-builder 1.0.1

* Mon Sep 06 2021 Evgeni Golov - 0.2.2-2
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.2.2-1
- Initial package.
