%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2024.8.30
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         certifi-2022.12.7-use-system-cert.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  ca-certificates

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Requires:       ca-certificates
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled Root Certificates collection
rm -rf certifi/*.pem


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2024.8.30-1
- Update to 2024.8.30

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2022.12.7-5
- Remove SCL bits

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
