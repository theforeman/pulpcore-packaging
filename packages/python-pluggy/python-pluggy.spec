%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pluggy

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.6.0
Release:        1%{?dist}
Summary:        plugin and hook calling mechanisms for python

License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove version_file key unsupported by RHEL 9 setuptools-scm
sed -i '/version_file/d' pyproject.toml

%build
set -ex
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.6.0-1
- Update to 1.6.0
- Fix build: pass SETUPTOOLS_SCM_PRETEND_VERSION to avoid missing git repo in mock
- Fix build: remove version_file key unsupported by RHEL 9 setuptools-scm

* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 1.5.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.0-1
- Update to 1.5.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3.0-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.3.0-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.3.0-2
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3.0-1
- Release python-pluggy 1.3.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.2.0-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa <osousa@redhat.com> - 1.2.0-1
- Initial package.
