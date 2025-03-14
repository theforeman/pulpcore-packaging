%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Disable debug
%define debug_package %{nil}
# Created by pyp2rpm-3.3.8
%global pypi_name dulwich

Name:           python-%{pypi_name}
Version:        0.21.7
Release:        1%{?dist}
Summary:        Python Git Library

License:        Apachev2 or later or GPLv2
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-setuptools-rust
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-urllib3 >= 1.24.1
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
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
%{python3_sitearch}/%{pypi_name}
%exclude %{_bindir}/dul-receive-pack
%exclude %{_bindir}/dul-upload-pack
%exclude %{_bindir}/%{pypi_name}
%exclude %{python3_sitearch}/docs/
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Mar 14 2025 Odilon Sousa <osousa@redhat.com> - 0.21.7-1
- Release python-dulwich 0.21.7

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.21.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.21.3-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 0.21.3-1
- Initial package.
