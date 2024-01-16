%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name pexpect

Name:           python-%{pypi_name}
Version:        4.8.0
Release:        6%{?dist}
Summary:        Pexpect allows easy control of interactive console applications

License:        ISC license
URL:            https://pexpect.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildArch:      noarch

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-ptyprocess


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.8.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.8.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.8.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.8.0-3
- Build against python 3.11

* Thu Sep 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.8.0-2
- Add requires on python-ptyprocess

* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.8.0-1
- Initial package.
