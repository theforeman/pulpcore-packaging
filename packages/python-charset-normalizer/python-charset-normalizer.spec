%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name charset-normalizer

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        5%{?dist}
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%exclude %{_bindir}/normalizer
%{python3_sitelib}/charset_normalizer
%{python3_sitelib}/charset_normalizer-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.1-5
- Remove SCL bits

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 2.1.1-4
- Dont obsolete python-charset-normalizer

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 2.1.1-1
- Update to 2.1.1

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-4
- Exclude files in bin for a better upgrade from python38 to python39 and removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.11-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-1
- Release python-charset-normalizer 2.0.11

* Mon Nov 01 2021 Odilon Sousa - 2.0.7-1
- Initial package.
