%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}
# Created by pyp2rpm-3.3.3
%global pypi_name ansible-lint
%global src_name ansible_lint

Name:           %{pypi_name}
Version:        24.7.0
Release:        1%{?dist}
Summary:        Checks playbooks for practices and behaviour that could potentially be improved

License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 7.0.5
BuildRequires:  python%{python3_pkgversion}-setuptools_scm_git_archive
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# This should be
# Requires:       (ansible >= 2.9 or ansible-core)
# But our tooling currently fails with rich deps
Requires:       /usr/bin/ansible
Requires:       python%{python3_pkgversion}-enrich >= 1.2.6
Requires:       python%{python3_pkgversion}-black >= 24.3.0
Requires:       python%{python3_pkgversion}-packaging >= 21.3
Requires:       python%{python3_pkgversion}-pyyaml >= 5.4.1 
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-jsonschema >= 4.10.0
Requires:       python%{python3_pkgversion}-filelock >= 3.3.0
Requires:       python%{python3_pkgversion}-rich >= 12.0.0 
Requires:       python%{python3_pkgversion}-ruamel-yaml < 1
Requires:       python%{python3_pkgversion}-ruamel-yaml >= 0.18.5
Requires:       python%{python3_pkgversion}-pathspec >= 0.10.3
Requires:       python%{python3_pkgversion}-subprocess-tee >= 0.4.1
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-tenacity
Requires:       python%{python3_pkgversion}-yamllint >= 1.30.0
Requires:       python%{python3_pkgversion}-wcmatch >= 8.1.2

%description
%{summary}

%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files
%{_bindir}/ansible-lint
%{python3_sitelib}/ansiblelint
%{python3_sitelib}/ansible_lint-%{version}.dist-info/

%changelog
* Mon Sep 16 2024 Odilon Sousa <osousa@redhat.com> - 24.7.0-1
- Release ansible-lint 24.7.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.4.0-1
- Release ansible-lint 5.4.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.0.8-5
- Build against python 3.11

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 5.0.8-4
- Rebuilding against python 3.9

* Tue Feb 22 2022 Odilon Sousa <osousa@redhat.com> - 5.0.8-3
- Require ansible OR ansible-core

* Mon Sep 13 2021 Evgeni Golov - 5.0.8-2
- Build against Python 3.8

* Fri May 14 2021 Evgeni Golov - 5.0.8-1
- Release ansible-lint 5.0.8

* Wed Mar 31 2021 Evgeni Golov - 5.0.6-1
- Update to 5.0.6

* Tue Nov 10 2020 Evgeni Golov 4.2.0-2
- fix requires

* Mon Jul 27 2020 Evgeni Golov 4.2.0-1
- package ansible-lint
