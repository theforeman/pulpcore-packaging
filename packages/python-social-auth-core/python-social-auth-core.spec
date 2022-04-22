%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name social-auth-core

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.4.0
Release:        2%{?dist}
Summary:        Python social authentication made simple

License:        BSD
URL:            https://github.com/python-social-auth/social-core
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyjwt >= 1.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 1.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-defusedxml >= 0.5.0rc1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-oauthlib >= 1.0.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-python3-openid >= 3.0.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.9.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests-oauthlib >= 0.6.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.10.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/social_core
%{python3_sitelib}/social_auth_core-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.4.0-2
- Build against python 3.9

* Mon Sep 13 2021 Evgeni Golov - 3.4.0-1
- Initial package.
