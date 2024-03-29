%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name humanfriendly

Name:           python-%{pypi_name}
Version:        10.0
Release:        7%{?dist}
Summary:        Human friendly output for text interfaces using Python

License:        MIT
URL:            https://humanfriendly.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%license LICENSE.txt
%doc docs/readme.rst README.rst
%exclude %{_bindir}/humanfriendly
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 10.0-7
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 10.0-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 10.0-5
- Build against python 3.11

* Tue Jun 14 2022 Odilon Sousa <osousa@redhat.com> - 10.0-4
- Exclude files in bin for a better upgrade from python38 to python39 and
  removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 10.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 10.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa - 10.0-1
- Initial package.
