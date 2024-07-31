
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.6
%global pypi_name pulp-cli

Name:           python-%{pypi_name}
Version:        0.27.1
Release:        1%{?dist}
Summary:        Command line interface to talk to pulpcore's REST API

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-PyYAML < 6.1
Requires:       python%{python3_pkgversion}-PyYAML >= 5.3
Requires:       python%{python3_pkgversion}-click < 9.0.0
Requires:       python%{python3_pkgversion}-click >= 8.0.0
Requires:       python%{python3_pkgversion}-click-shell < 3
Requires:       python%{python3_pkgversion}-click-shell >= 2.1
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pygments
Requires:       python%{python3_pkgversion}-requests < 2.32
Requires:       python%{python3_pkgversion}-requests >= 2.24.0
Requires:       python%{python3_pkgversion}-schema < 0.8
Requires:       python%{python3_pkgversion}-schema >= 0.7.5
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-toml < 0.11
Requires:       python%{python3_pkgversion}-toml >= 0.10.2
Requires:       python%{python3_pkgversion}-pulp-glue == 0.27.1

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

Provides:       %{pypi_name} = %{version}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}



%prep
set -ex
%autosetup -n %{pypi_name}-%{version}

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/pulp
%{python3_sitelib}/pulp_cli
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pytest_pulp_cli
%{python3_sitelib}/pulp_cli-%{version}.dist-info/


%changelog
* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 0.27.1-1
- Release python-pulp-cli 0.27.1

* Tue Jun 18 2024 Odilon Sousa <osousa@redhat.com> - 0.25.6-1
- Release python-pulp-cli 0.25.6

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 0.25.4-1
- Release python-pulp-cli 0.25.4

* Mon Jun 03 2024 Evgeni Golov - 0.25.3-1
- Release python-pulp-cli 0.25.3

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 0.25.1-1
- Release python-pulp-cli 0.25.1

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 0.23.2-1
- Release python-pulp-cli 0.23.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.21.2-5
- Remove SCL bits

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 0.21.2-4
- Fix PyYAML deps for pulp-cli version

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.21.2-3
- Obsolete python39 packages for a smooth upgrade

* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 0.21.2-2
- Rebuild against python 3.11

* Thu Sep 14 2023 Quirin Pamp <pamp@atix.de> - 0.21.2-1
- Update python-pulp-cli to 0.21.2.

* Thu Sep 08 2022 Odilon Sousa <osousa@redhat.com> - 0.14.0-4
- Bump python-pulp-cli release to rebuild for python 3.9

* Fri May 27 2022 Odilon Sousa <osousa@redhat.com> - 0.14.0-2
- Bump release to rebuild against python39

* Thu May 26 2022 Odilon Sousa <osousa@redhat.com> - 0.14.0-1
- Release python-pulp-cli 0.14.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.12.0-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.12.0-3
- Build against python 3.9

* Mon Mar 28 2022 Evgeni Golov - 0.12.0-2
- Add provides for pulp-cli
- Add SCL wrapper so /usr/bin/pulp always works

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 0.12.0-1
- Release python-pulp-cli 0.12.0

* Wed Sep 29 2021 Evgeni Golov - 0.11.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 13 2021 Evgeni Golov - 0.11.0-2
- Build against Python 3.8

* Wed Aug 11 2021 Evgeni Golov - 0.11.0-1
- Release python-pulp-cli 0.11.0

* Wed Jun 30 2021 Evgeni Golov - 0.10.1-1
- Initial package.

