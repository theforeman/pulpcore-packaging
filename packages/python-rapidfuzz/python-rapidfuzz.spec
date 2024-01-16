%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global debug_package %{nil}

# Created by pyp2rpm-3.3.8
%global pypi_name rapidfuzz

Name:           python-%{pypi_name}
Version:        2.15.1
Release:        5%{?dist}
Summary:        rapid fuzzy string matching

License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.15.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.15.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.15.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.15.1-2
- Build against python 3.11

* Fri Aug 04 2023 Odilon Sousa <osousa@redhat.com> - 2.15.1-1
- Initial package.
