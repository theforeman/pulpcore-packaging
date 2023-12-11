%global pkg_name %{name}
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.7
%global pypi_name pulp_manifest

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        4%{?dist}
Summary:        Tool to generate a PULP_MANIFEST file for a given directory, so the directory can be recognized by Pulp

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://codeload.github.com/pulp/pulp-manifest/tar.gz/%{version}#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n pulp-manifest-%{version}



%build
set -ex
%py3_build



%install
set -ex
%py3_install



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp-manifest
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Dec 11 2023 Odilon Sousa <osousa@redhat.com> - 3.0.0-4
- Bump pulp-manifest release to rebuild against python 3.11

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 3.0.0-3
- Bump release on python-pulp-manifest for a rebuild on python 3.9

* Tue Sep 06 2022 Odilon Sousa <osousa@redhat.com> - 3.0.0-2
- Bump release on python-pulp-manifest for a rebuild on python 3.8

* Fri Oct 08 2021 Evgeni Golov - 3.0.0-1
- Initial package.
