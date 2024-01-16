%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.2
%global pypi_name setuptools_scm_git_archive

Name:           python-%{pypi_name}
Version:        1.4.1
Release:        4%{?dist}
Summary:        setuptools_scm plugin for git archives

License:        MIT
URL:            https://github.com/Changaco/setuptools_scm_git_archive/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-typing-extensions

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-setuptools


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.4.1-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.4.1-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.4.1-2
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.4.1-1
- Release python-setuptools_scm_git_archive 1.4.1

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.1-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane - 1.1-3
- Build against Python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.1-2
- Build against Python 3.8

* Mon Aug 03 2020 Evgeni Golov - 1.1-1
- Initial package.
