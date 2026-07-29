%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name cachetools

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        6.2.4
Release:        2%{?dist}
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://github.com/tkem/cachetools
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%autosetup -n %{pypi_name}-%{version}
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 6.2.4-2
- Bump release for EL10 rebuild

* Mon Jan 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 6.2.4-1
- Update to 6.2.4
- Fix PEP 639 license format in pyproject.toml

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.2.2-1
- Update to 6.2.2

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.2.1-1
- Update to 6.2.1

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 5.5.2-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.5.2-1
- Update to 5.5.2

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.5.1-1
- Update to 5.5.1

* Mon Sep 23 2024 Odilon Sousa - 5.5.0-1
- Initial package.
