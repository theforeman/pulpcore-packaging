%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name commonmark

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        9%{?dist}
Summary:        Python parser for the CommonMark Markdown spec

License:        BSD-3-Clause
URL:            https://github.com/rtfd/commonmark.py
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-future >= 0.14.0
Requires:       python%{python3_pkgversion}-setuptools


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
%exclude %{_bindir}/cmark
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.9.1-9
- Remove SCL bits

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 0.9.1-8
- Dont obsolete python-commonmark

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.9.1-7
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.9.1-6
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.9.1-5
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 0.9.1-4
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 0.9.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 0.9.1-2
- Build against Python 3.8

* Tue Aug 25 2020 Evgeni Golov - 0.9.1-1
- Initial package.
