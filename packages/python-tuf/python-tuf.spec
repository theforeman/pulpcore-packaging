%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name tuf

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        7.0.0
Release:        2%{?dist}
Summary:        A Framework for Securing Software Update Systems

License:        Apache-2.0 OR MIT
URL:            https://www.updateframework.com
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-securesystemslib >= 1.0
Conflicts:      python%{python3_pkgversion}-securesystemslib >= 2.0
Requires:       python%{python3_pkgversion}-urllib3 >= 1.21.1
Requires:       python%{python3_pkgversion}-urllib3 < 3

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
%license LICENSE LICENSE-MIT
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 7.0.0-2
- Bump release for EL10 rebuild

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 7.0.0-1
- Update to 7.0.0

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 6.0.0-1
- Initial package.
