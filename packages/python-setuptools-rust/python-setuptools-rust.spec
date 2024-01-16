%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name setuptools-rust

Name:           python-%{pypi_name}
Version:        1.6.0
Release:        4%{?dist}
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 41
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 3.4.3
BuildRequires:  python%{python3_pkgversion}-wheel


%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-semantic-version >= 2.6
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.7.4


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
%{python3_sitelib}/setuptools_rust
%{python3_sitelib}/setuptools_rust-*-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.6.0-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-2
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.6.0-1
- Release python-setuptools-rust 1.6.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.11.5-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane - 0.11.5-2
- Build against python 3.9.

* Thu Sep 09 2021 Evgeni Golov - 0.11.5-1
- Initial package.
