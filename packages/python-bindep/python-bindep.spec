%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name bindep

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.12.0
Release:        2%{?dist}
Summary:        Binary dependency utility

License:        Apache License, Version 2.0
URL:            https://docs.opendev.org/opendev/bindep
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr >= 2.0.0
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-Parsley
Requires:       python%{python3_pkgversion}-distro >= 1.7.0
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pbr >= 2.0.0
Requires:       python%{python3_pkgversion}-setuptools

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
%doc README.rst doc/source/readme.rst
%exclude %{_bindir}/bindep
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 2.12.0-2
- Rebuild against python3.12

* Sun Jan 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.12.0-1
- Update to 2.12.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.11.0-5
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.11.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.11.0-3
- Build against python 3.11

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 2.11.0-2
- Changing dependencies to reflect the setup config for python >= 3.6

* Tue Sep 20 2022 Odilon Sousa 2.11.0-1
- Update to 2.11.0

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 2.10.2-4
- Exclude files in bin for a better upgrade from python38 to python39 and
  removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 2.10.2-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.2-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.10.2-1
- Release python-bindep 2.10.2

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.10.1-1
- Release python-bindep 2.10.1

* Wed Sep 08 2021 Evgeni Golov - 2.9.0-1
- Initial package.
