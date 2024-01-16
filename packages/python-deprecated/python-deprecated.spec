%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name Deprecated
%global srcname deprecated

Name:           python-%{srcname}
Version:        1.2.13
Release:        5%{?dist}
Summary:        Python @deprecated decorator to deprecate old python classes, functions or methods

License:        MIT
URL:            https://github.com/tantale/deprecated
Source0:        https://files.pythonhosted.org/packages/source/D/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-wrapt >= 1.10
Conflicts:      python%{python3_pkgversion}-wrapt >= 2


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
%license LICENSE.rst docs/source/license.rst
%doc README.md
%{python3_sitelib}/deprecated
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.2.13-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.2.13-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.2.13-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.2.13-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa - 1.2.13-1
- Initial package.
