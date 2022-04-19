%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        36.0.2
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-hypothesis = 3.79.2
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.8.0
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 3.1.0
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 3.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bcrypt >= 3.1.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-black
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8-import-order
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-iso8601
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pep8-naming
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pretend
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyenchant >= 1.6.11
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-subtests
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytz
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-rust >= 0.11.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-twine >= 1.12.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-hypothesis = 3.79.2
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-sphinx = 1.8.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-sphinx = 3.1.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-sphinx = 3.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bcrypt >= 3.1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-black
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flake8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flake8-import-order
Requires:       %{?scl_prefix}python%{python3_pkgversion}-hypothesis >= 1.11.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-iso8601
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pep8-naming
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pretend
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyenchant >= 1.6.11
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-subtests
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytz
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools-rust >= 0.11.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx >= 1.6.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-rtd-theme
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinxcontrib-spelling >= 4.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-twine >= 1.12.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE LICENSE.APACHE LICENSE.BSD LICENSE.PSF
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 19 2022 Yanis Guenane 36.0.2-1
- Update to 36.0.2

* Mon Sep 13 2021 Evgeni Golov - 3.1.1-1
- Release python-cryptography 3.1.1

* Wed Sep 08 2021 Evgeni Golov - 2.9.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 2.9.2-1
- Update to 2.9.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
