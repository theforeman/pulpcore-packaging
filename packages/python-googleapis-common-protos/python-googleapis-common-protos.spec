%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name googleapis-common-protos

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.59.1
Release:        4%{?dist}
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 3.20.0
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 3.20.1
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.1
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.2
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.3
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.4
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-protobuf < 5.0.0.dev0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-protobuf >= 3.19.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 3.20.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 3.20.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.2
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.3
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.4
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-protobuf = 4.21.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio < 2.0.0.dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-grpcio >= 1.44.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf < 5.0.0.dev0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf >= 3.19.5


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.59.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.59.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.59.1-2
- Build against python 3.11

* Wed Jul 05 2023 Odilon Sousa - 1.59.1-1
- Initial package.
