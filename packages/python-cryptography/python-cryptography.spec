# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildConflicts: python3-cffi = 1.11.3
BuildConflicts: python3-cffi = 1.11.3
BuildConflicts: python3-hypothesis = 3.79.2
BuildConflicts: python3-pytest = 3.9.0
BuildConflicts: python3-pytest = 3.9.1
BuildConflicts: python3-pytest = 3.9.2
BuildConflicts: python3-sphinx = 1.8.0
BuildConflicts: python3-sphinx = 3.1.0
BuildConflicts: python3-sphinx = 3.1.1
BuildRequires:  python3-bcrypt >= 3.1.5
BuildRequires:  python3-black
BuildRequires:  python3-cffi >= 1.8
BuildRequires:  python3-cffi >= 1.8
BuildRequires:  python3-doc8
BuildRequires:  python3-enum34
BuildRequires:  python3-flake8
BuildRequires:  python3-flake8-import-order
BuildRequires:  python3-hypothesis >= 1.11.4
BuildRequires:  python3-ipaddress
BuildRequires:  python3-iso8601
BuildRequires:  python3-pep8-naming
BuildRequires:  python3-pretend
BuildRequires:  python3-pyenchant >= 1.6.11
BuildRequires:  python3-pytest >= 3.6.0
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.4.1
BuildRequires:  python3-twine >= 1.12.0

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Conflicts:      python3-cffi = 1.11.3
Conflicts:      python3-hypothesis = 3.79.2
Conflicts:      python3-pytest = 3.9.0
Conflicts:      python3-pytest = 3.9.1
Conflicts:      python3-pytest = 3.9.2
Conflicts:      python3-sphinx = 1.8.0
Conflicts:      python3-sphinx = 3.1.0
Conflicts:      python3-sphinx = 3.1.1
Requires:       python3-bcrypt >= 3.1.5
Requires:       python3-black
Requires:       python3-cffi >= 1.8
Requires:       python3-doc8
Requires:       python3-enum34
Requires:       python3-flake8
Requires:       python3-flake8-import-order
Requires:       python3-hypothesis >= 1.11.4
Requires:       python3-ipaddress
Requires:       python3-iso8601
Requires:       python3-pep8-naming
Requires:       python3-pretend
Requires:       python3-pyenchant >= 1.6.11
Requires:       python3-pytest >= 3.6.0
Requires:       python3-pytz
Requires:       python3-six >= 1.4.1
Requires:       python3-sphinx >= 1.6.5
Requires:       python3-sphinx-rtd-theme
Requires:       python3-sphinxcontrib-spelling >= 4.0.1
Requires:       python3-twine >= 1.12.0

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
%license LICENSE LICENSE.APACHE LICENSE.BSD LICENSE.PSF
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 3.1.1-1
- Update to 3.1.1

* Tue Apr 28 2020 Evgeni Golov 2.9.2-1
- Update to 2.9.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
