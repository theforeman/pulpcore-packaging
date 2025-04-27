%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name Pillow
%global srcname pillow

Name:           python%{python3_pkgversion}-%{srcname}
Version:        11.1.0
Release:        1%{?dist}
Summary:        Python Imaging Library (Fork)

License:        HPND
URL:            https://python-pillow.org
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{srcname}-%{version}.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitearch}/PIL
%{python3_sitearch}/%{srcname}-%{version}.dist-info/

%changelog
* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 11.1.0-1
- Update to 11.1.0

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 10.3.0-2
- Rebuild against python3.12

* Thu Aug 01 2024 Odilon Sousa <osousa@redhat.com> - 10.3.0-1
- Release python-pillow 10.3.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 9.5.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 9.5.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 9.5.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 9.5.0-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa - 9.5.0-1
- Initial package.
