%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-deb

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-debian < 0.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-debian >= 0.1.44
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore < 3.40
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.28
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gnupg < 0.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gnupg >= 0.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jsonschema < 5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jsonschema >= 4.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(deb) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

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
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 06 2023 Quirin Pamp <pamp@atix.de> - 3.0.0-1
- Update to 3.0.0

* Tue Sep 05 2023 Quirin Pamp <pamp@atix.de> - 2.21.2-1
- Update to 2.21.2

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 2.21.1-1
- Release python-pulp-deb 2.21.1

* Wed May 03 2023 Quirin Pamp <pamp@atix.de> - 2.20.2-1
- Update to 2.20.2

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 2.20.1-1
- Release python-pulp-deb 2.20.1

* Sun Oct 23 2022 Odilon Sousa <osousa@redhat.com> - 2.20.0-1
- Release python-pulp-deb 2.20.0

* Tue Sep 20 2022 Odilon Sousa 2.19.0-1
- Update to 2.19.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 2.18.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 2.18.0-2
- Rebuilding against python 3.9

* Tue Apr 26 2022 Quirin Pamp <pamp@atix.de> - 2.18.0-1
- Update to 2.18.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.17.0-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 2.17.0-1
- Release python-pulp-deb 2.17.0

* Thu Jan 13 2022 Quirin Pamp - 2.16.1-1
- Update to 2.16.1

* Thu Nov 11 2021 Quirin Pamp - 2.16.0-1
- Update to 2.16.0

* Mon Oct 18 2021 Evgeni Golov - 2.15.0-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Wed Sep 08 2021 Evgeni Golov 2.15.0-1
- Update to 2.15.0

* Mon Aug 02 2021 Quirin Pamp 2.14.1-1
- Update to 2.14.1

* Fri Jun 11 2021 Evgeni Golov 2.13.0-1
- Update to 2.13.0

* Tue May 25 2021 Quirin Pamp 2.11.2-1
- Update to 2.11.2

* Thu Apr 15 2021 Quirin Pamp 2.11.1-1
- Update to 2.11.1

* Fri Mar 19 2021 Evgeni Golov 2.10.0-1
- Update to 2.10.0

* Mon Jan 11 2021 Evgeni Golov 2.8.0-1
- Update to 2.8.0

* Wed Sep 30 2020 Evgeni Golov - 2.7.0-1
- Release python-pulp-deb 2.7.0

* Thu Sep 03 2020 Evgeni Golov 2.6.1-1
- Update to 2.6.1

* Thu Jun 18 2020 Evgeni Golov - 2.4.0-0.1.b1
- Update to 2.4.0b1

* Thu Apr 30 2020 ATIX AG <info@atix.de> - 2.3.0-0.1.b1
- Initial package.
