%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name MarkupPy
%global srcname markuppy

Name:           python%{python3_pkgversion}-%{srcname}
Version:        1.18
Release:        1%{?dist}
Summary:        An HTML/XML generator

License:        MIT
URL:            https://github.com/tylerbakke/MarkupPy
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


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


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.18-1
- Update to 1.18

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 1.14-8
- Rebuild against python 3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.14-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.14-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.14-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.14-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.14-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.14-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov - 1.14-1
- Initial package.
