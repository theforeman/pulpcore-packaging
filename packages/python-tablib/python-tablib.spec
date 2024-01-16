%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name tablib

Name:           python-%{pypi_name}
Version:        3.3.0
Release:        5%{?dist}
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:        MIT
URL:            https://tablib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-typing-extensions

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-markuppy
Requires:       python%{python3_pkgversion}-odfpy
Requires:       python%{python3_pkgversion}-openpyxl >= 2.6.0
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-xlrd
Requires:       python%{python3_pkgversion}-xlwt

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}


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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.3.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.3.0-4
- Rollback overzealous obsoletes

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.3.0-1
- Update to 3.3.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.0-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 3.2.0-1
- Release python-tablib 3.2.0

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.1.0-1
- Release python-tablib 3.1.0

* Tue Oct 19 2021 Evgeni Golov - 3.0.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 3.0.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Jun 04 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Tue Apr 28 2020 Evgeni Golov - 1.1.0-1
- Initial package.
