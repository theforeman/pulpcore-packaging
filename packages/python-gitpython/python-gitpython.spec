%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name GitPython
%global srcname gitpython

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.1.26
Release:        1%{?dist}
Summary:        GitPython is a python library used to interact with Git repositories

License:        BSD
URL:            https://github.com/gitpython-developers/GitPython
Source0:        https://files.pythonhosted.org/packages/source/G/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-ddt = 1.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ddt >= 1.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8-bugbear
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8-comprehensions
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8-typing-imports
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gitdb < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gitdb < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gitdb >= 4.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gitdb >= 4.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-sugar
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.7.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 3.7.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-virtualenv


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
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
%{python3_sitelib}/__pycache__/git/__init__.*
%{python3_sitelib}/git/__init__.py
%{python3_sitelib}/__pycache__/git/cmd.*
%{python3_sitelib}/git/cmd.py
%{python3_sitelib}/__pycache__/git/compat.*
%{python3_sitelib}/git/compat.py
%{python3_sitelib}/__pycache__/git/config.*
%{python3_sitelib}/git/config.py
%{python3_sitelib}/__pycache__/git/db.*
%{python3_sitelib}/git/db.py
%{python3_sitelib}/__pycache__/git/diff.*
%{python3_sitelib}/git/diff.py
%{python3_sitelib}/__pycache__/git/exc.*
%{python3_sitelib}/git/exc.py
%{python3_sitelib}/__pycache__/git/index/__init__.*
%{python3_sitelib}/git/index/__init__.py
%{python3_sitelib}/__pycache__/git/index/base.*
%{python3_sitelib}/git/index/base.py
%{python3_sitelib}/__pycache__/git/index/fun.*
%{python3_sitelib}/git/index/fun.py
%{python3_sitelib}/__pycache__/git/index/typ.*
%{python3_sitelib}/git/index/typ.py
%{python3_sitelib}/__pycache__/git/index/util.*
%{python3_sitelib}/git/index/util.py
%{python3_sitelib}/__pycache__/git/objects/__init__.*
%{python3_sitelib}/git/objects/__init__.py
%{python3_sitelib}/__pycache__/git/objects/base.*
%{python3_sitelib}/git/objects/base.py
%{python3_sitelib}/__pycache__/git/objects/blob.*
%{python3_sitelib}/git/objects/blob.py
%{python3_sitelib}/__pycache__/git/objects/commit.*
%{python3_sitelib}/git/objects/commit.py
%{python3_sitelib}/__pycache__/git/objects/fun.*
%{python3_sitelib}/git/objects/fun.py
%{python3_sitelib}/__pycache__/git/objects/submodule/__init__.*
%{python3_sitelib}/git/objects/submodule/__init__.py
%{python3_sitelib}/__pycache__/git/objects/submodule/base.*
%{python3_sitelib}/git/objects/submodule/base.py
%{python3_sitelib}/__pycache__/git/objects/submodule/root.*
%{python3_sitelib}/git/objects/submodule/root.py
%{python3_sitelib}/__pycache__/git/objects/submodule/util.*
%{python3_sitelib}/git/objects/submodule/util.py
%{python3_sitelib}/__pycache__/git/objects/tag.*
%{python3_sitelib}/git/objects/tag.py
%{python3_sitelib}/__pycache__/git/objects/tree.*
%{python3_sitelib}/git/objects/tree.py
%{python3_sitelib}/__pycache__/git/objects/util.*
%{python3_sitelib}/git/objects/util.py
%{python3_sitelib}/__pycache__/git/refs/__init__.*
%{python3_sitelib}/git/refs/__init__.py
%{python3_sitelib}/__pycache__/git/refs/head.*
%{python3_sitelib}/git/refs/head.py
%{python3_sitelib}/__pycache__/git/refs/log.*
%{python3_sitelib}/git/refs/log.py
%{python3_sitelib}/__pycache__/git/refs/reference.*
%{python3_sitelib}/git/refs/reference.py
%{python3_sitelib}/__pycache__/git/refs/remote.*
%{python3_sitelib}/git/refs/remote.py
%{python3_sitelib}/__pycache__/git/refs/symbolic.*
%{python3_sitelib}/git/refs/symbolic.py
%{python3_sitelib}/__pycache__/git/refs/tag.*
%{python3_sitelib}/git/refs/tag.py
%{python3_sitelib}/__pycache__/git/remote.*
%{python3_sitelib}/git/remote.py
%{python3_sitelib}/__pycache__/git/repo/__init__.*
%{python3_sitelib}/git/repo/__init__.py
%{python3_sitelib}/__pycache__/git/repo/base.*
%{python3_sitelib}/git/repo/base.py
%{python3_sitelib}/__pycache__/git/repo/fun.*
%{python3_sitelib}/git/repo/fun.py
%{python3_sitelib}/__pycache__/git/types.*
%{python3_sitelib}/git/types.py
%{python3_sitelib}/__pycache__/git/util.*
%{python3_sitelib}/git/util.py
%{python3_sitelib}/git
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Feb 07 2022 Odilon Sousa - 3.1.26-1
- Initial package.
