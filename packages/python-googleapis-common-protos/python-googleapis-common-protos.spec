%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name googleapis-common-protos
%global srcname googleapis_common_protos

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.69.0
Release:        2%{?dist}
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildConflicts: python%{python3_pkgversion}-protobuf = 3.20.0
BuildConflicts: python%{python3_pkgversion}-protobuf = 3.20.1
BuildConflicts: python%{python3_pkgversion}-protobuf = 4.21.1
BuildConflicts: python%{python3_pkgversion}-protobuf = 4.21.2
BuildConflicts: python%{python3_pkgversion}-protobuf = 4.21.3
BuildConflicts: python%{python3_pkgversion}-protobuf = 4.21.4
BuildConflicts: python%{python3_pkgversion}-protobuf = 4.21.5
BuildRequires:  python%{python3_pkgversion}-protobuf < 5.0.0.dev0
BuildRequires:  python%{python3_pkgversion}-protobuf >= 3.19.5
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Conflicts:      python%{python3_pkgversion}-protobuf = 3.20.0
Conflicts:      python%{python3_pkgversion}-protobuf = 3.20.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.1
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.2
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.3
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.4
Conflicts:      python%{python3_pkgversion}-protobuf = 4.21.5
Requires:       python%{python3_pkgversion}-grpcio < 2.0.0.dev0
Requires:       python%{python3_pkgversion}-grpcio >= 1.44.0
Requires:       python%{python3_pkgversion}-protobuf < 5.0.0.dev0
Requires:       python%{python3_pkgversion}-protobuf >= 3.19.5

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%exclude %{python3_sitelib}/docs
%{python3_sitelib}/google
%{python3_sitelib}/googleapis_common_protos-%{version}.dist-info/


%changelog
* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 1.69.0-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.69.0-1
- Update to 1.69.0

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.66.0-1
- Update to 1.66.0

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.65.0-1
- Update to 1.65.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.59.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.59.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.59.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.59.1-2
- Build against python 3.11

* Wed Jul 05 2023 Odilon Sousa - 1.59.1-1
- Initial package.
