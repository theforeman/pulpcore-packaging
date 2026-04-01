%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name msgpack

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.1.2
Release:        1%{?dist}
Summary:        MessagePack serializer

License:        Apache 2.0
URL:            https://msgpack.org/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}




%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 pip does not support SPDX string format)
sed -i 's/^license = \"\(.*\)\"/license = {text = \"\1\"}/' pyproject.toml
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
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.2-1
- Update to 1.1.2
- Fix PEP 639 license field for RHEL 9 pip compatibility

* Fri Jun 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.1-1
- Update to 1.1.1

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 1.1.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.0-1
- Update to 1.1.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.5-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.5-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.5-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.5-2
- Build against python 3.11

* Thu Aug 03 2023 Odilon Sousa <osousa@redhat.com> - 1.0.5-1
- Initial package.
