# Created by pyp2rpm-3.3.3
%global pypi_name python-gnupg
%global srcname gnupg

Name:           python-%{srcname}
Version:        0.4.7
Release:        1%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        BSD-3-Clause
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/gnupg.*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 0.4.7-1
- Update to 0.4.7

* Tue Apr 28 2020 Evgeni Golov 0.4.6-1
- Update to 0.4.6

* Wed Mar 18 2020 Samir Jha - 0.4.5-1
- Initial package.
