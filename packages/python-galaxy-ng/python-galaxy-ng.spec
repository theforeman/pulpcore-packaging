# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-ng

Name:           python-%{pypi_name}
Version:        4.2.0
Release:        1%{?dist}
Summary:        galaxy-ng plugin for the Pulp Project

License:        GPLv2+
URL:            https://github.com/ansible/galaxy_ng/
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 2.2.3
Conflicts:      python%{python3_pkgversion}-django >= 2.3
Requires:       python%{python3_pkgversion}-django-prometheus >= 2.0.0
Requires:       python%{python3_pkgversion}-drf-spectacular
Requires:       python%{python3_pkgversion}-galaxy-importer >= 0.2.11
Requires:       python%{python3_pkgversion}-galaxy-importer < 0.2.12
Requires:       python%{python3_pkgversion}-pulp-ansible >= 1:0.5.0
Conflicts:      python%{python3_pkgversion}-pulp-ansible >= 1:0.6
Requires:       python%{python3_pkgversion}-pulpcore < 3.9
Requires:       python%{python3_pkgversion}-pulpcore >= 3.7
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitelib}/galaxy_ng
%{python3_sitelib}/galaxy_ng-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 13 2020 Evgeni Golov 4.2.0-1
- Update to 4.2.0

* Thu Nov 05 2020 Evgeni Golov 4.2.0-0.1.rc3
- Update to 4.2.0rc3

* Tue Nov 03 2020 Evgeni Golov 4.2.0-0.1.rc2
- Update to 4.2.0rc2

* Mon Oct 05 2020 Evgeni Golov 4.2.0-0.1.rc1
- Update to 4.2.0rc1

* Mon Sep 28 2020 Evgeni Golov 4.2.0-0.1.b3
- Update to 4.2.0b3

* Thu Sep 17 2020 Evgeni Golov 4.2.0-0.1.b2
- Update to 4.2.0b2

* Mon Sep 14 2020 Evgeni Golov 4.2.0-0.1.b1
- Update to 4.2.0b1

* Fri Jul 17 2020 Evgeni Golov - 4.2.0-0.1.a10
- Initial package.
