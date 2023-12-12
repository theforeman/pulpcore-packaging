%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name certifi

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2022.12.7
Release:        4%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         certifi-2022.12.7-use-system-cert.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  ca-certificates

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Requires:       ca-certificates
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled Root Certificates collection
rm -rf certifi/*.pem
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2022.12.7-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2022.12.7-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2022.12.7-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2022.12.7-1
- Update to 2022.12.7

* Tue Apr 26 2022 Yanis Guenane - 2020.6.20-3
- Build against Python 3.9

* Wed Sep 08 2021 Evgeni Golov - 2020.6.20-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov - 2020.6.20-1
- Initial package.
