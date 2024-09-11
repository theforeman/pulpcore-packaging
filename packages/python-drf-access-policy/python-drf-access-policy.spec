%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name drf-access-policy

Name:           python-%{pypi_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        Declarative access policies/permissions modeled after AWS' IAM policies

License:        MIT
URL:            https://github.com/rsinger86/drf-access-policy
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-djangorestframework
Requires:       python%{python3_pkgversion}-pyparsing

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/rest_access_policy
%{python3_sitelib}/drf_access_policy-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.0-1
- Update to 1.5.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.3.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.3.0-1
- Update to 1.3.0

* Tue Sep 20 2022 Odilon Sousa 1.1.2-1
- Update to 1.1.2

* Fri May 13 2022 Yanis Guenane <yguenane@redhat.com> - 1.1.0-3
- Obsolete Python 3.8 package

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.1.0-2
- Build against python 3.9

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 1.1.0-1
- Release python-drf-access-policy 1.1.0

* Wed Sep 08 2021 Evgeni Golov 1.0.1-1
- Update to 1.0.1

* Mon Sep 06 2021 Evgeni Golov - 0.9.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 0.9.0-1
- Update to 0.9.0

* Fri Mar 19 2021 Evgeni Golov 0.8.7-1
- Update to 0.8.7

* Mon Nov 02 2020 Evgeni Golov 0.8.1-1
- Update to 0.8.1

* Mon Sep 28 2020 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Tue Aug 25 2020 Evgeni Golov - 0.6.2-1
- Initial package.
