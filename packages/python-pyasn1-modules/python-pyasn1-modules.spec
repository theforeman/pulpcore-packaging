%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name pyasn1-modules
%global src_name pyasn1_modules

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        1%{?dist}
Summary:        A collection of ASN.1-based protocols modules

License:        BSD-2-Clause
URL:            https://github.com/pyasn1/pyasn1-modules
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyasn1 >= 0.4.6
Requires:       python%{python3_pkgversion}-pyasn1 < 0.7.0


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Oct 22 2024 Odilon Sousa <osousa@redhat.com> - 0.4.1-1
- Release python-pyasn1-modules 0.4.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.2.8-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.2.8-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.2.8-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.2.8-2
- Build against python 3.11

* Thu Aug 25 2022 Odilon Sousa <osousa@redhat.com> - 0.2.8-1
- Initial package.
