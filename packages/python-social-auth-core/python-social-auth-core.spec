%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name social-auth-core

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        6%{?dist}
Summary:        Python social authentication made simple

License:        BSD
URL:            https://github.com/python-social-auth/social-core
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six >= 1.10.0


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyjwt >= 1.4.0
Requires:       python%{python3_pkgversion}-cryptography >= 1.4
Requires:       python%{python3_pkgversion}-defusedxml >= 0.5.0rc1
Requires:       python%{python3_pkgversion}-oauthlib >= 1.0.3
Requires:       python%{python3_pkgversion}-python3-openid >= 3.0.10
Requires:       python%{python3_pkgversion}-requests >= 2.9.1
Requires:       python%{python3_pkgversion}-requests-oauthlib >= 0.6.1
Requires:       python%{python3_pkgversion}-six >= 1.10.0


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
%{python3_sitelib}/social_core
%{python3_sitelib}/social_auth_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.4.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.4.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.4.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.4.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.4.0-2
- Build against python 3.9

* Mon Sep 13 2021 Evgeni Golov - 3.4.0-1
- Initial package.
