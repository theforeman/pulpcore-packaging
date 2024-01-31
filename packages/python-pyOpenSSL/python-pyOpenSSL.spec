%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pyOpenSSL
%global srcname pyopenssl

Name:           python-%{pypi_name}
Version:        23.3.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library

License:        Apache License, Version 2.0
URL:            https://pyopenssl.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-cryptography >= 41.0.5
Requires:       python%{python3_pkgversion}-cryptography < 42


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/OpenSSL
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jan 31 2024 Odilon Sousa <osousa@redhat.com> - 23.3.0-1
- Release python-pyOpenSSL 23.3.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 22.1.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 22.1.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 22.1.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 22.1.0-2
- Build against python 3.11

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 22.1.0-1
- Release python-pyOpenSSL 22.1.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 19.1.0-3
- Build against python 3.9

* Wed Sep 08 2021 Evgeni Golov - 19.1.0-2
- Build against Python 3.8

* Thu Apr 30 2020 Evgeni Golov - 19.1.0-1
- Initial package.
