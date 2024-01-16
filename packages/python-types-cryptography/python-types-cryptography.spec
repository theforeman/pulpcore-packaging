%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name types-cryptography

Name:           python-%{pypi_name}
Version:        3.3.23.2
Release:        5%{?dist}
Summary:        Typing stubs for cryptography

License:        Apache-2.0 license
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%{python3_sitelib}/cryptography-stubs
%{python3_sitelib}/types_cryptography-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.3.23.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.3.23.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.3.23.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.23.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.3.23.2-1
- Update to 3.3.23.2

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 3.3.23-1
- Initial package.
