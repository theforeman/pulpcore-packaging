%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable debug
%define debug_package %{nil}
# Created by pyp2rpm-3.3.8
%global pypi_name dulwich

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.2.10
Release:        2%{?dist}
Summary:        Python Git Library

License:        Apachev2 or later or GPLv2
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
### Older versions of setuptools can't handle new LICENSE files structure
Patch0:         0001-Revert-pyproject.toml-fix-warnings-change.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-setuptools-rust
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-urllib3 >= 2.2.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel

%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%exclude %{_bindir}/dul-receive-pack
%exclude %{_bindir}/dul-upload-pack
%exclude %{_bindir}/%{pypi_name}
%exclude %{python3_sitearch}/docs/
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 1.2.10-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.10-1
- Update to 1.2.10

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.6-1
- Update to 1.2.6
- Update urllib3 minimum requirement to >= 2.2.2 (upstream 1.2.6 requires urllib3 >= 2.2.2)

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.1-1
- Update to 1.2.1

* Wed Apr 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 18 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.0-1
- Update to 1.1.0

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.24.6-1
- Update to 0.24.6

* Thu Oct 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.24.2-1
- Update to 0.24.2

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.21.7-3
- Add obsoletes for python3.11 package

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 0.21.7-2
- Rebuild against python3.12

* Fri Mar 14 2025 Odilon Sousa <osousa@redhat.com> - 0.21.7-1
- Release python-dulwich 0.21.7

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.21.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.21.3-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 0.21.3-1
- Initial package.
