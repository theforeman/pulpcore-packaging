%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name importlib-metadata

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        8.7.1
Release:        1%{?dist}
Summary:        Read metadata from Python packages

License:        Apache Software License
URL:            http://importlib-metadata.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-zipp >= 3.20

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n importlib_metadata-%{version}
# Fix PEP 639 metadata for the older setuptools available on RHEL
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
# coherent.licensed is not packaged on RHEL and is not required for the sdist
sed -i '/"coherent.licensed"/d' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/importlib_metadata
%{python3_sitelib}/importlib_metadata-%{version}.dist-info/


%changelog
* Thu Sep  3 21:40:21 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 8.7.1-1
- Update to 8.7.1
- Switch to the pyproject wheel build
- Patch PEP 639 metadata for RHEL setuptools compatibility

* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 6.0.1-8
- Bump release for EL10 rebuild

* Wed Jul 22 2026 Odilon Sousa <osousa@redhat.com> - 6.0.1-7
- Restore package: python3.12-opentelemetry_api and python3.12-bandersnatch
  declare importlib-metadata as an unconditional (non-marker-gated) upstream
  dependency, so it was incorrectly removed in the EL10 obsolete-package
  cleanup (#2766), breaking nightly repoclosure

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 6.0.1-6
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 6.0.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 6.0.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 6.0.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.0.1-2
- Build against python 3.11

* Mon Jul 03 2023 Odilon Sousa <osousa@redhat.com> - 6.0.1-1
- Release python-importlib-metadata 6.0.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.10.1-2
- Build against python 3.9

* Wed Feb 23 2022 Odilon Sousa <osousa@redhat.com> - 4.10.1-1
- Release python-importlib-metadata 4.10.1

* Wed Sep 08 2021 Evgeni Golov - 1.7.0-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov 1.7.0-1
- Update to 1.7.0

* Thu Jun 18 2020 Evgeni Golov 1.6.1-1
- Update to 1.6.1

* Thu Jun 04 2020 Evgeni Golov 1.6.0-1
- Update to 1.6.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 1.4.0-1
- Initial package.
