%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pyasn1

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.6.4
Release:        1%{?dist}
Summary:        ASN.1 types and codecs

License:        BSD
URL:            https://github.com/etingof/pyasn1
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.rst docs/source/license.rst
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Aug 11 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.6.4-1
- Update to 0.6.4

* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 0.6.3-2
- Bump release for EL10 rebuild

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.6.3-1
- Update to 0.6.3
- Switch to pyproject build (setup.py removed upstream)

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 0.6.1-2
- Rebuild against python3.12

* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.6.1-1
- Update to 0.6.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.4.8-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.4.8-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4.8-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.8-2
- Build against python 3.11

* Thu Aug 25 2022 Odilon Sousa <osousa@redhat.com> - 0.4.8-1
- Initial package.
