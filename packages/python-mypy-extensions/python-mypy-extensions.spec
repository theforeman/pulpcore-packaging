%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name mypy-extensions
%global src_name mypy_extensions

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Type system extensions for mypy

License:        MIT
URL:            https://github.com/python/mypy_extensions
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Fix PEP 639 license string (RHEL 9 flit_core does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitelib}/__pycache__/%{src_name}.*
%{python3_sitelib}/%{src_name}.py
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 1.1.0-2
- Bump release for EL10 rebuild

* Fri Jun 12 2026 Odilon Sousa <osousa@redhat.com> - 1.1.0-1
- Initial package
