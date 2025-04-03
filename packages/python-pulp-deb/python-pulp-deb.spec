%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-deb
%global src_name pulp_deb

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.5.1
Release:        2%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-debian < 0.2.0
Requires:       python%{python3_pkgversion}-debian >= 0.1.44
Requires:       python%{python3_pkgversion}-pulpcore < 3.85
Requires:       python%{python3_pkgversion}-pulpcore >= 3.49
Requires:       python%{python3_pkgversion}-gnupg < 0.6
Requires:       python%{python3_pkgversion}-gnupg >= 0.5
Requires:       python%{python3_pkgversion}-jsonschema < 5.0
Requires:       python%{python3_pkgversion}-jsonschema >= 4.6

Provides:       pulpcore-plugin(deb) = %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}



%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}.dist-info/

%changelog
* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 3.5.1-2
- Rebuild python-pulp-deb against python3.12

* Mon Feb 24 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.1-1
- Update to 3.5.1

* Tue Jan 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.0-1
- Update to 3.5.0

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.1-1
- Update to 3.3.1

* Wed Aug 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.1-1
- Update to 3.2.1

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 3.2.0-1
- Release python-pulp-deb 3.2.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.0.1-2
- Remove SCL bits

* Tue Dec 12 2023 Quirin Pamp <pamp@atix.de> - 3.0.1-1
- Update to 3.0.1

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.0.0-3
- Obsolete python39 packages for a smooth upgrade

* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 3.0.0-2
- Rebuild against python 3.11

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
