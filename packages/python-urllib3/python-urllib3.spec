# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.26.6
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst dummyserver/certs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 13 2021 Evgeni Golov 1.26.6-1
- Update to 1.26.6

* Thu Jul 08 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.26.5-1
- Release python-urllib3 1.26.5

* Fri Mar 19 2021 Evgeni Golov 1.26.4-1
- Update to 1.26.4

* Thu Oct 29 2020 Evgeni Golov 1.25.11-1
- Update to 1.25.11

* Mon Aug 10 2020 Evgeni Golov 1.25.10-1
- Update to 1.25.10

* Tue Apr 28 2020 Evgeni Golov 1.25.9-1
- Update to 1.25.9

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.25.8-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 1.25.8-1
- Update to 1.25.8

* Mon Nov 18 2019 Evgeni Golov - 1.25.7-1
- Initial package.
