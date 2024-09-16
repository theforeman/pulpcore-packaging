%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name python-debian
%global srcname debian

Name:           python-%{srcname}
Version:        0.1.49
Release:        1%{?dist}
Summary:        Debian package related modules

License:        GPL-2+
URL:            https://salsa.debian.org/python-debian-team/python-debian
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-chardet
Requires:       zstd


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
%doc README.rst
%{python3_sitelib}/__pycache__/deb822.*
%{python3_sitelib}/deb822.py
%{python3_sitelib}/debian
%{python3_sitelib}/debian_bundle
%{python3_sitelib}/python_debian-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.1.49-1
- Update to 0.1.49

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.1.44-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.1.44-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.1.44-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.1.44-4
- Build against python 3.11

* Wed Aug 24 2022 Quirin Pamp <pamp@atix.de> - 0.1.44-3
- Bump release to 3 to ensure a smooth upgrade from the 3.16 repo.

* Thu Aug 18 2022 Quirin Pamp <pamp@atix.de> - 0.1.44-1
- Update to 0.1.44
- Add zstd dependency to support zstd compression for Ubuntu.

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.1.43-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa 0.1.43-1
- Update to 0.1.43

* Wed Nov 03 2021 Odilon Sousa 0.1.42-1
- Update to 0.1.42

* Wed Sep 08 2021 Evgeni Golov - 0.1.40-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov 0.1.40-1
- Update to 0.1.40

* Fri Mar 19 2021 Evgeni Golov 0.1.39-1
- Update to 0.1.39

* Thu Oct 29 2020 Evgeni Golov 0.1.38-1
- Update to 0.1.38

* Thu Apr 30 2020 Markus Bucher <bucher@atix.de> - 0.1.37-1
- Initial package.
