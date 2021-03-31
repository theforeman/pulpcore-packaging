# Created by pyp2rpm-3.3.3
%global pypi_name ansible-lint

Name:           %{pypi_name}
Version:        5.0.6
Release:        1%{?dist}
Summary:        Checks playbooks for practices and behaviour that could potentially be improved

License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 3.5.0
BuildRequires:  python%{python3_pkgversion}-setuptools_scm_git_archive

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       ansible >= 2.9
Requires:       python%{python3_pkgversion}-enrich >= 1.2.6
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-rich >= 9.5.1
Requires:       python%{python3_pkgversion}-ruamel-yaml < 1
Requires:       python%{python3_pkgversion}-ruamel-yaml >= 0.15.37
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-typing-extensions
Requires:       python%{python3_pkgversion}-wcmatch >= 7.0

%description
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst docs/README.md examples/playbooks/README.md test/local-content/README.md
%{_bindir}/ansible-lint
%{python3_sitelib}/ansiblelint
%{python3_sitelib}/ansible_lint-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 31 2021 Evgeni Golov - 5.0.6-1
- Update to 5.0.6

* Tue Nov 10 2020 Evgeni Golov 4.2.0-2
- fix requires

* Mon Jul 27 2020 Evgeni Golov 4.2.0-1
- package ansible-lint
