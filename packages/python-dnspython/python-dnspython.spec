%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name dnspython

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.9.1
Release:        1%{?dist}
Summary:        DNS toolkit for Python

License:        ISC
URL:            https://www.dnspython.org
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        dnspython-2.9.0-LICENSE
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-uv-build >= 0.9.21
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/dns
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Oct 30 20:36:25 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.9.1-1
- Update to 2.9.1
- Keep the SPDX license string when license-files is present.

* Wed Oct 14 04:28:46 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.9.0-1
- Update to 2.9.0
- Use uv-build as the build backend
- Include the upstream LICENSE omitted from the source archive

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 2.8.0-2
- Bump release for EL10 rebuild

* Wed Apr 15 2026 Odilon Sousa <osousa@redhat.com> - 2.8.0-1
- Initial package.
