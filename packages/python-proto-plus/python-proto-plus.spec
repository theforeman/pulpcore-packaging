%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name proto-plus
%global src_name proto_plus

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.28.3
Release:        1%{?dist}
Summary:        Beautiful, Pythonic protocol buffers.

License:        Apache 2.0
URL:            https://github.com/googleapis/proto-plus-python
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-protobuf >= 3.19.0
Requires:       python%{python3_pkgversion}-protobuf < 7

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/proto
%{python3_sitelib}/proto_plus-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Aug 09 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.28.3-1
- Update to 1.28.3

* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 1.28.0-2
- Bump release for EL10 rebuild

* Sun May 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.28.0-1
- Update to 1.28.0

* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.27.2-1
- Update to 1.27.2

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.27.1-1
- Update to 1.27.1

* Wed Jan 21 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.27.0-1
- Update to 1.27.0

* Tue Mar 25 2025 Odilon Sousa <osousa@redhat.com> - 1.26.1-2
- Rebuild against python3.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.26.1-1
- Update to 1.26.1

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.26.0-1
- Update to 1.26.0

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.25.0-1
- Update to 1.25.0

* Mon Sep 23 2024 Odilon Sousa - 1.24.0-1
- Initial package.
