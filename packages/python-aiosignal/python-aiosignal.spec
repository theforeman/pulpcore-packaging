%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name aiosignal

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.3.2
Release:        2%{?dist}
Summary:        aiosignal: a list of registered asynchronous callbacks

License:        Apache 2.0
URL:            https://github.com/aio-libs/aiosignal
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-frozenlist >= 1.1.0
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-frozenlist >= 1.1.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 1.3.2-2
- Rebuild against python3.12

* Wed Dec 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.3.2-1
- Update to 1.3.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.3.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.3.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3.1-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.3.1-1
- Update to 1.3.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.2.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa - 1.2.0-1
- Initial package.
