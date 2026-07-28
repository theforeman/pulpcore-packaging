%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name defusedxml

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.7.1
Release:        9%{?dist}
Summary:        XML bomb protection for Python stdlib modules

License:        PSFL
URL:            https://github.com/tiran/defusedxml
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

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
%doc README.html README.md README.txt other/README.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 0.7.1-9
- Bump release for EL10 rebuild

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 0.7.1-8
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.7.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.7.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.7.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.7.1-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.7.1-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.7.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.7.1-1
- Update to 0.7.1

* Tue Apr 28 2020 Evgeni Golov - 0.6.0-1
- Initial package.
