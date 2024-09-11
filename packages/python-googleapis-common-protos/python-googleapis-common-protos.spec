%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name googleapis-common-protos
%global srcname googleapis_common_protos

Name:           python-%{pypi_name}
Version:        1.65.0
Release:        1%{?dist}
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


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
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


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}.egg-info


%changelog
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
