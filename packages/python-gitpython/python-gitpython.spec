%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name GitPython
%global srcname gitpython

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.1.32
Release:        2%{?dist}
Summary:        GitPython is a python library used to interact with Git repositories

License:        BSD
URL:            https://github.com/gitpython-developers/GitPython
Source0:        https://files.pythonhosted.org/packages/source/G/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       git-core
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gitdb < 5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gitdb >= 4.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.7.4.3


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/git
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.1.32-2
- Build against python 3.11

* Mon Aug 28 2023 Odilon Sousa <osousa@redhat.com> - 3.1.32-1
- Release python-gitpython 3.1.32
- Fix for CVE-2022-24439

* Thu Mar 09 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.1.30-2
- Depend on git-core instead of git

* Mon Jan 23 2023 Odilon Sousa <osousa@redhat.com> - 3.1.30-1
- Release python-gitpython 3.1.30
- Fix for CVE-2022-24439

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.1.26-3
- Build against python 3.9

* Thu Mar 17 2022 Odilon Sousa <osousa@redhat.com> - 3.1.26-2
- Adding git as a dependency for git-python 

* Mon Feb 07 2022 Odilon Sousa - 3.1.26-1
- Initial package.
