# Created by pyp2rpm-3.3.3
%global pypi_name python-debian
%global srcname debian

Name:           python-%{srcname}
Version:        0.1.40
Release:        1%{?dist}
Summary:        Debian package related modules

License:        GPL-2+
URL:            https://salsa.debian.org/python-debian-team/python-debian
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-chardet
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-chardet
Requires:       python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{python3_sitelib}/__pycache__/deb822.*
%{python3_sitelib}/deb822.py
%{python3_sitelib}/debian
%{python3_sitelib}/debian_bundle
%{python3_sitelib}/python_debian-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov 0.1.40-1
- Update to 0.1.40

* Fri Mar 19 2021 Evgeni Golov 0.1.39-1
- Update to 0.1.39

* Thu Oct 29 2020 Evgeni Golov 0.1.38-1
- Update to 0.1.38

* Thu Apr 30 2020 Markus Bucher <bucher@atix.de> - 0.1.37-1
- Initial package.
