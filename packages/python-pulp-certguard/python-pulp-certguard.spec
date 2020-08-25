# Created by pyp2rpm-3.3.3
%global pypi_name pulp-certguard

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Certguard plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulp-certguard.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pyOpenSSL
Requires:       python3-pulpcore < 3.7
Requires:       python3-pulpcore >= 3.3
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_certguard-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 25 2020 Evgeni Golov 1.0.2-1
- Update to 1.0.2

* Fri Jun 19 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-0.2.rc5
- Adjust pyopenssl requires to pyOpenSSL

* Wed May 27 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0-0.1.rc5
- Update to 0.1.rc5

* Thu Apr 30 2020 Evgeni Golov - 0.1.0-0.1.rc4
- Initial package.
