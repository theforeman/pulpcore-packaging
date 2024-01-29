%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name ansible-builder

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        A tool for building Ansible Execution Environments

License:        Apache-2.0
URL:            https://github.com/ansible/ansible-builder/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-toml
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-bindep
Requires:       python%{python3_pkgversion}-requirements-parser
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif
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
%{_bindir}/ansible-builder
%{python3_sitelib}/ansible_builder
%{python3_sitelib}/ansible_builder-%{version}.dist-info/

%changelog
* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 3.0.0-1
- Release python-ansible-builder 3.0.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.1-7
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.0.1-6
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.1-5
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.1-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.1-3
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 1.0.1-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Fri Sep 10 2021 Evgeni Golov - 1.0.1-1
- Release python-ansible-builder 1.0.1

* Mon Sep 06 2021 Evgeni Golov - 0.2.2-2
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.2.2-1
- Initial package.
