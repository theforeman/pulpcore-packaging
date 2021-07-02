# Created by pyp2rpm-3.3.3
%global pypi_name pulp-certguard

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Certguard plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulp-certguard.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyOpenSSL
Requires:       python%{python3_pkgversion}-pulpcore < 3.15
Requires:       python%{python3_pkgversion}-pulpcore >= 3.10
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_certguard-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 02 2021 Evgeni Golov - 1.4.0-1
- Release python-pulp-certguard 1.4.0

* Fri Jun 11 2021 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Fri Mar 19 2021 Evgeni Golov 1.2.0-1
- Update to 1.2.0

* Mon Jan 11 2021 Evgeni Golov 1.1.0-1
- Update to 1.1.0

* Mon Sep 28 2020 Evgeni Golov 1.0.3-1
- Update to 1.0.3

* Tue Aug 25 2020 Evgeni Golov 1.0.2-1
- Update to 1.0.2

* Fri Jun 19 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-0.2.rc5
- Adjust pyopenssl requires to pyOpenSSL

* Wed May 27 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0-0.1.rc5
- Update to 0.1.rc5

* Thu Apr 30 2020 Evgeni Golov - 0.1.0-0.1.rc4
- Initial package.
