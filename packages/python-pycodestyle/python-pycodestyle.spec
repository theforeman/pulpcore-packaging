%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pycodestyle

Name:           python-%{pypi_name}
Version:        2.11.1
Release:        1%{?dist}
Summary:        Python style guide checker

License:        Expat license
URL:            https://pycodestyle.pycqa.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

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
%exclude %{_bindir}/pycodestyle
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.11.1-1
- Update to 2.11.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.9.1-3
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.9.1-2
- Add python39 obsoletes to package

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 2.9.1-1
- Release python-pycodestyle 2.9.1

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.7.0-6
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.7.0-5
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 2.7.0-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 2.7.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.7.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.7.0-1
- Update to 2.7.0

* Tue Jun 23 2020 Evgeni Golov - 2.6.0-1
- Initial package.
