%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name yamllint

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.38.0
Release:        1%{?dist}
Summary:        A linter for YAML files

License:        GPLv3+
URL:            https://github.com/adrienverge/yamllint
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-pathspec >= 1.0.0
Requires:       python%{python3_pkgversion}-pyyaml

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license string (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%exclude %{_bindir}/yamllint
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jun 12 2026 Odilon Sousa <osousa@redhat.com> - 1.38.0-1
- Initial package
