%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-ansible

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.10.0
Release:        2%{?dist}
Epoch:          1
Summary:        Pulp plugin to manage Ansible content, e.g. roles

License:        GPLv2+
URL:            https://github.com/pulp/pulp_ansible
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML
Requires:       %{?scl_prefix}python%{python3_pkgversion}-async-lru >= 1.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-async-lru >= 1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-galaxy-importer >= 0.3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jsonschema >= 3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.17
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.15.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-semantic-version
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(ansible) = %{version}
Obsoletes:      python3-%{pypi_name} < %{epoch}:%{version}-%{release}

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
%doc README.rst
%{python3_sitelib}/pulp_ansible
%{python3_sitelib}/pulp_ansible-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 18 2021 Evgeni Golov - 1:0.10.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name
- Fix Epoch that was forgotten in 0.10.0-1

* Wed Sep 08 2021 Evgeni Golov 0.10.0-1
- Update to 0.10.0

* Thu Jul 29 2021 Odilon Sousa <osousa@redhat.com> - 1:0.9.0-1
- Release python-pulp-ansible 0.9.0

* Wed Jul 28 2021 Odilon Sousa <osousa@redhat.com> - 1:0.8.1-1
- Release python-pulp-ansible 0.8.1

* Fri Jun 11 2021 Evgeni Golov 1:0.8.0-1
- Update to 0.8.0

* Wed May 12 2021 Evgeni Golov 1:0.7.3-1
- Update to 0.7.3

* Fri Mar 19 2021 Evgeni Golov 1:0.7.1-1
- Update to 0.7.1

* Mon Jan 11 2021 Evgeni Golov 1:0.6.0-1
- Update to 0.6.0

* Fri Dec 18 2020 Evgeni Golov - 1:0.5.5-1
- Release python-pulp-ansible 0.5.5

* Wed Dec 09 2020 Evgeni Golov - 1:0.5.4-1
- Release python-pulp-ansible 0.5.4

* Wed Dec 09 2020 Evgeni Golov - 1:0.5.3-1
- Release python-pulp-ansible 0.5.3

* Thu Nov 26 2020 Evgeni Golov - 1:0.5.2-1
- Release python-pulp-ansible 0.5.2

* Tue Nov 10 2020 Evgeni Golov - 1:0.5.1-1
- Release python-pulp-ansible 0.5.1

* Tue Nov 03 2020 Evgeni Golov 1:0.5.0-1
- Update to 0.5.0

* Fri Oct 23 2020 Evgeni Golov - 1:0.4.2-1
- Release python-pulp-ansible 0.4.2

* Thu Oct 01 2020 Evgeni Golov - 1:0.4.1-1
- Release python-pulp-ansible 0.4.1

* Mon Sep 28 2020 Evgeni Golov 1:0.4.0-1
- Update to 0.4.0

* Thu Sep 10 2020 Evgeni Golov 1:0.3.0-1
- Update to 0.3.0

* Tue Aug 25 2020 Evgeni Golov 1:0.2.0-1
- Update to 0.2.0

* Mon Aug 10 2020 Evgeni Golov 0.2.0b15-1
- Update to 0.2.0b15

* Mon Jul 27 2020 Evgeni Golov - 0.2.0b14-2
* Fix pyyaml dependency

* Tue Jun 23 2020 Evgeni Golov - 0.2.0b14-1
- Initial package.
