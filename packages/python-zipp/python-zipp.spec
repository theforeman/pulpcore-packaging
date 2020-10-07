# Created by pyp2rpm-3.3.3
%global pypi_name zipp

Name:           python-%{pypi_name}
Version:        3.3.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        None
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3-pytest = 3.7.3
BuildRequires:  python3-func-timeout
BuildRequires:  python3-jaraco-itertools
BuildRequires:  python3-jaraco-packaging >= 3.2
BuildRequires:  python3-jaraco-test >= 3.2.0
BuildRequires:  python3-pytest >= 3.5
BuildRequires:  python3-pytest-black >= 0.3.7
BuildRequires:  python3-pytest-checkdocs >= 1.2.3
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-flake8
BuildRequires:  python3-pytest-mypy
BuildRequires:  python3-rst-linker >= 1.9
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm >= 3.4.1

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Conflicts:      python3-pytest = 3.7.3
Requires:       python3-func-timeout
Requires:       python3-jaraco-itertools
Requires:       python3-jaraco-packaging >= 3.2
Requires:       python3-jaraco-test >= 3.2.0
Requires:       python3-pytest >= 3.5
Requires:       python3-pytest-black >= 0.3.7
Requires:       python3-pytest-checkdocs >= 1.2.3
Requires:       python3-pytest-cov
Requires:       python3-pytest-flake8
Requires:       python3-pytest-mypy
Requires:       python3-rst-linker >= 1.9
Requires:       python3-sphinx

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 3.3.0-1
- Update to 3.3.0

* Thu Jun 04 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 2.1.0-1
- Initial package.
