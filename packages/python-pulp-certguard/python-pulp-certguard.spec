%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-certguard

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.5.0
Release:        2%{?dist}
Summary:        Certguard plugin for the Pulp Project

License:        GPLv2+
URL:            https://docs.pulpproject.org/pulp_certguard/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyOpenSSL
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.10
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(certguard) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.


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
%doc README.rst
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_certguard-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 18 2021 Evgeni Golov - 1.5.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 1.5.0-1
- Update to 1.5.0

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
