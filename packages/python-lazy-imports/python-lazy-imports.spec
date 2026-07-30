%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name lazy-imports
%global src_name lazy_imports

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Tool to support lazy imports

License:        Apache-2.0
URL:            https://github.com/bachorp/lazy-imports
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Fri Jul 31 2026 Odilon Sousa <osousa@redhat.com> - 1.2.0-2
- Rebuild for EL10

* Thu Mar 26 2026 Odilon Sousa <osousa@redhat.com> - 1.2.0-1
- Initial package.
