# Created by pyp2rpm-3.3.3
%global pypi_name pycares

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Python interface for c-ares

License:        MIT
URL:            http://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.5.0
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-cffi >= 1.5.0
Requires:       python%{python3_pkgversion}-idna >= 2.1

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE deps/c-ares/LICENSE.md
%doc README.rst deps/c-ares/README.cares deps/c-ares/README.md deps/c-ares/README.msvc deps/c-ares/test/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 11 2021 Evgeni Golov 4.0.0-1
- Update to 4.0.0

* Thu Nov 05 2020 Evgeni Golov - 3.1.1-2
- Fix License tag in spec file

* Wed Mar 18 2020 Samir Jha - 3.1.1-1
- Initial package.
