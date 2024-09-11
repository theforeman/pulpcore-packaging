%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name grpcio
%global srcname grpcio

Name:           python-%{srcname}
Version:        1.66.1
Release:        1%{?dist}
Summary:        HTTP/2-based RPC framework

License:        Apache License 2.0
URL:            https://grpc.io
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build

%install
set -ex
%py3_install



%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/grpc
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.66.1-1
- Update to 1.66.1

* Mon Aug 12 2024 Odilon Sousa <osousa@redhat.com> - 1.65.4-1
- Release python-grpcio 1.65.4

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.56.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.56.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.56.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.56.0-2
- Build against python 3.11

* Wed Jul 05 2023 Odilon Sousa <osousa@redhat.com> - 1.56.0-1
- Initial package.
