%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        6.1.0
Release:        1%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co

License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-mccabe < 0.8.0
Requires:       python%{python3_pkgversion}-mccabe >= 0.7.0
Requires:       python%{python3_pkgversion}-pycodestyle < 2.12.0
Requires:       python%{python3_pkgversion}-pycodestyle >= 2.11.0
Requires:       python%{python3_pkgversion}-pyflakes < 3.2.0
Requires:       python%{python3_pkgversion}-pyflakes >= 3.1.0
Requires:       python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

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
%doc README.rst tests/fixtures/config_files/README.rst
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.0-1
- Update to 6.1.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 5.0.0-3
- Remove SCL bits

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 5.0.0-2
- Fix requires for flake8 5.0.0

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 5.0.0-1
- Release python-flake8 5.0.0

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.9.2-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.9.2-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.9.2-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.9.2-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 3.9.2-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.9.2-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 3.9.2-1
- Update to 3.9.2

* Fri Mar 19 2021 Evgeni Golov 3.9.0-1
- Update to 3.9.0

* Thu Oct 29 2020 Evgeni Golov 3.8.4-1
- Update to 3.8.4

* Tue Jun 23 2020 Evgeni Golov - 3.8.3-1
- Initial package.
