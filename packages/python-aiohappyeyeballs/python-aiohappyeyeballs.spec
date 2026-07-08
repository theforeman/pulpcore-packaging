%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name aiohappyeyeballs

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.7.1
Release:        1%{?dist}
Summary:        This library exists to allow connecting with Happy Eyeballs (RFC 8305) when you already have a list of addrinfo and not a DNS name.

License:        Python Software Foundation License 2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry_core

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

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.1-1
- Update to 2.7.1

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.6.2-1
- Update to 2.6.2

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.6.1-1
- Update to 2.6.1

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 2.4.4-2
- Rebuild against python3.12

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.4-1
- Update to 2.4.4

* Tue Oct 29 2024 Odilon Sousa - 2.4.3-1
- Initial package.
