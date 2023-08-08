# Created by pyp2rpm-3.3.8
%global pypi_name dulwich

Name:           python-%{pypi_name}
Version:        0.21.3
Release:        1%{?dist}
Summary:        Python Git Library

License:        Apachev2 or later or GPLv2
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-pip


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-urllib3 >= 1.24.1


%description -n python%{python3_pkgversion}-%{pypi_name}
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


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%exclude %{_bindir}/dul-receive-pack
%exclude %{_bindir}/dul-upload-pack
%exclude %{_bindir}/%{pypi_name}
%exclude %{python3_sitearch}/docs/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 0.21.3-1
- Initial package.
