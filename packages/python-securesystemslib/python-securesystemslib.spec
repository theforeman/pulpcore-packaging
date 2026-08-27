%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name securesystemslib

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        A library that provides cryptographic and general-purpose routines

License:        MIT
URL:            https://github.com/secure-systems-lab/securesystemslib
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Aug 27 11:20:27 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.0-1
- Update to 1.5.0

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 1.4.0-2
- Bump release for EL10 rebuild

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.0-1
- Update to 1.4.0

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 1.3.1-1
- Initial package.
