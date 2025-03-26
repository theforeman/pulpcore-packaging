%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name enrich

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.2.6
Release:        10%{?dist}
Summary:        enrich

License:        MIT
URL:            https://github.com/pycontribs/enrich
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 3.5.0
BuildRequires:  python%{python3_pkgversion}-setuptools_scm_git_archive >= 1.1
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-rich >= 9.5.1

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description
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
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 1.2.6-10
- Rebuild against python3.12

* Tue Apr 30 2024 Odilon Sousa <osousa@redhat.com> - 1.2.6-9
- Rebuild with new package metadata

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.2.6-8
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.2.6-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.2.6-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 1.2.6-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.2.6-4
- Build against python 3.9

* Wed Oct 20 2021 Evgeni Golov - 1.2.6-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 1.2.6-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov - 1.2.6-1
- Initial package.
