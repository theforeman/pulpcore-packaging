%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global pypi_name build

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.5.0
Release:        2%{?dist}
Summary:        A simple, correct Python build frontend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/build
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core

Requires:       python%{python3_pkgversion}-packaging >= 19.0
Requires:       python%{python3_pkgversion}-pyproject_hooks
Requires:       python%{python3_pkgversion}-tomli >= 1.1.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
%{_bindir}/pyproject-build


%changelog
* Mon Jul 20 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.5.0-2
- Drop importlib-metadata requirement

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.0-1
- Update to 1.5.0

* Sun Apr 26 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.4-1
- Update to 1.4.4

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.3-1
- Update to 1.4.3

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.2-1
- Update to 1.4.2

* Mon Apr 07 2025 Odilon Sousa <osousa@redhat.com> - 1.2.2-3
- Add obsolete for python3.11 package

* Fri Mar 21 2025 Odilon Sousa <osousa@redhat.com> - 1.2.2-2
- Rebuild against python3.12

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.2-1
- Update to 1.2.2.post1

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.10.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.10.0-2
- Build against python 3.11

* Thu Aug 03 2023 Odilon Sousa - 0.10.0-1
- Initial package.