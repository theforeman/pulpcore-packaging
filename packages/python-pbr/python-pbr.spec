%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pbr

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        6.1.1
Release:        3%{?dist}
Summary:        Python Build Reasonableness

License:        None
URL:            https://docs.openstack.org/pbr/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.32.0

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
%license LICENSE pbr/tests/testpackage/LICENSE.txt
%doc README.rst pbr/tests/testpackage/README.txt
%exclude %{_bindir}/pbr
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 6.1.1-3
- Add obsoletes for python3.11 package

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 6.1.1-2
- Rebuild against python3.12

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.1-1
- Update to 6.1.1

* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.0-1
- Update to 6.1.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 5.8.0-7
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 5.8.0-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.8.0-5
- Build against python 3.11

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-4
- Exclude files in bin for a better upgrade from python38 to python39 and
  removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-2
- Rebuild against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-1
- Release python-pbr 5.8.0

* Wed Sep 08 2021 Evgeni Golov - 5.6.0-1
- Initial package.
