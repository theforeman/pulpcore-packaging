# Created by pyp2rpm-3.3.3
%global pypi_name attrs

Name:           python-%{pypi_name}
Version:        20.2.0
Release:        1%{?dist}
Summary:        Classes Without Boilerplate

License:        MIT
URL:            https://www.attrs.org/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-coverage >= 5.0.2
BuildRequires:  python3-coverage >= 5.0.2
BuildRequires:  python3-coverage >= 5.0.2
BuildRequires:  python3-hypothesis
BuildRequires:  python3-hypothesis
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pre-commit
BuildRequires:  python3-pympler
BuildRequires:  python3-pympler
BuildRequires:  python3-pympler
BuildRequires:  python3-pytest >= 4.3.0
BuildRequires:  python3-pytest >= 4.3.0
BuildRequires:  python3-pytest >= 4.3.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-six
BuildRequires:  python3-six
BuildRequires:  python3-zope-interface
BuildRequires:  python3-zope-interface
BuildRequires:  python3-zope-interface
BuildRequires:  python3-zope-interface

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-coverage >= 5.0.2
Requires:       python3-coverage >= 5.0.2
Requires:       python3-hypothesis
Requires:       python3-hypothesis
Requires:       python3-pympler
Requires:       python3-pympler
Requires:       python3-pytest >= 4.3.0
Requires:       python3-pytest >= 4.3.0
Requires:       python3-six
Requires:       python3-six
Requires:       python3-sphinx
Requires:       python3-sphinx-rtd-theme
Requires:       python3-zope-interface
Requires:       python3-zope-interface

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
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/attr
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 20.2.0-1
- Update to 20.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 19.3.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 19.3.0-1
- Initial package.
