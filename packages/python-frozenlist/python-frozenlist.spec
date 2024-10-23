%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name frozenlist

Name:           python-%{pypi_name}
Version:        1.4.1
Release:        1%{?dist}
Summary:        A list-like structure which implements collections

License:        Apache 2
URL:            https://github.com/aio-libs/frozenlist
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.1-1
- Update to 1.4.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.3.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.3.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3.3-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.3.3-1
- Update to 1.3.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.3.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa - 1.3.0-1
- Initial package.
