%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12


# Created by pyp2rpm-3.3.3
%global pypi_name pulp-ostree
%global src_name pulp_ostree

 
Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.4.8
Release:        1%{?dist}
Summary:        Ostree plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}%{?prerelease}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Provides:       pulpcore-plugin(ostree) = %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pulpcore >= 3.49.0
Requires:       python%{python3_pkgversion}-pulpcore < 3.85
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?rhel} == 9 && "%{?python3_pkgversion}" != "3.12"
Requires:       python%{python3_pkgversion}-gobject >= 3.40.1
Requires:       python%{python3_pkgversion}-gobject < 3.51
%else
Requires:       python%{python3_pkgversion}-pygobject >= 1:3.40.1
Requires:       python%{python3_pkgversion}-pygobject < 1:3.51
%endif
Requires:       ostree

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
A Pulp plugin to support hosting ostree repositories.

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
%{python3_sitelib}/pulp_ostree
%{python3_sitelib}/pulp_ostree-%{version}.dist-info/


%changelog
* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.8-1
- Update to 2.4.8

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 2.4.7-2
- Add obsoletes for python3.11 package

* Fri Apr 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.7-1
- Update to 2.4.7

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.4.6-2
- Rebuild against python3.12

* Tue Feb 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.6-1
- Update to 2.4.6

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.4-1
- Update to 2.4.4

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.3-1
- Update to 2.4.3

* Mon Jul 22 2024 Odilon Sousa <osousa@redhat.com> - 2.3.2-1
- Release python-pulp-ostree 2.3.2

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 2.3.0-1
- Release python-pulp-ostree 2.3.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.3-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 2.1.3-3
- Obsolete python39 packages for a smooth upgrade

* Thu Nov 16 2023 Patrick Creech <pcreech@redhat.com> - 2.1.3-2
- Use pygobject dependency if we aren't using system python

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 2.1.3-1
- Release python-pulp-ostree 2.1.3

* Fri Aug 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.1-1
- Release python-pulp-ostree 2.1.1

* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 2.0.0-0.8.a6
- Release python-pulp-ostree 2.0.0a6

* Fri Jun 17 2022 Evgeni Golov - 2.0.0-0.7.a5
- Obsolete the old Python 3.8 package for smooth upgrade

* Mon May 30 2022 Odilon Sousa <osousa@redhat.com> - 2.0.0-0.6.a5
- Removing EPOCH requirement on EL9

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 2.0.0-0.5.a5
- Release python-pulp-ostree 2.0.0a5

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.0-0.4.a4
- Build against python 3.9

* Thu Jan 27 2022 Evgeni Golov - 2.0.0-0.3.a4
- Update pygobject dependency to include epoch

* Mon Jan 17 2022 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.2.a4
- update to 2.0.0a4

* Thu Dec 02 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.2.a2
- fix pygobject requires

* Wed Oct 20 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.1.a2
- initial build

