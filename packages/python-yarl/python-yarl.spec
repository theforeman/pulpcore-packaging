# Created by pyp2rpm-3.3.3
%global pypi_name yarl

Name:           python-%{pypi_name}
Version:        1.6.3
Release:        1%{?dist}
Summary:        Yet another URL library

License:        Apache 2
URL:            https://github.com/aio-libs/yarl/
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-idna >= 2.0
BuildRequires:  python%{python3_pkgversion}-multidict >= 4.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-typing-extensions >= 3.7.4

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-idna >= 2.0
Requires:       python%{python3_pkgversion}-multidict >= 4.0
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.7.4

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
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 1.6.3-1
- Update to 1.6.3

* Thu Oct 29 2020 Evgeni Golov 1.6.2-1
- Update to 1.6.2

* Mon Aug 10 2020 Evgeni Golov 1.5.1-1
- Update to 1.5.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Mon Nov 18 2019 Evgeni Golov - 1.3.0-1
- Initial package.
