%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%{?python_disable_dependency_generator}


# Created by pyp2rpm-3.3.8
%global pypi_name grpcio
%global srcname grpcio

Name:           %{?scl_prefix}python-%{srcname}
Version:        1.56.0
Release:        3%{?dist}
Summary:        HTTP/2-based RPC framework

License:        Apache License 2.0
URL:            https://grpc.io
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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



%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/grpc
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.56.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.56.0-2
- Build against python 3.11

* Wed Jul 05 2023 Odilon Sousa <osousa@redhat.com> - 1.56.0-1
- Initial package.
