
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.7
%global pypi_name pulp-cli-deb
%global pkg_name pulp_cli_deb

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Command line interface (CLI) for Pulp's pulp_deb plugin.

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli-deb
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

Requires:       python%{python3_pkgversion}-pulp-cli >= 0.23.2
Requires:       python%{python3_pkgversion}-pulp-cli < 0.28
Requires:       python%{python3_pkgversion}-click
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-pulp-glue-deb == %{version}

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
%{python3_sitelib}/pulpcore
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/


%changelog
* Tue Aug 27 2024 Quirin Pamp <pamp@atix.de> - 0.2.0-2
- Use version macro for python-pulp-glue-deb dependency

* Tue Aug 06 2024 Odilon Sousa <osousa@redhat.com> - 0.2.0-1
- Release python-pulp-cli-deb 0.2.0

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 0.1.0-1
- Release python-pulp-cli-deb 0.1.0

* Thu Feb 29 2024 Quirin Pamp <pamp@atix.de> - 0.0.7-1
- Update python-pulp-cli-deb to 0.0.7.

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.0.5-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.0.5-3
- Obsolete python39 packages for a smooth upgrade

* Thu Nov 16 2023 Odilon Sousa <osousa@redhat.com> - 0.0.5-2
- Rebuild against python 3.11

* Thu Sep 14 2023 Quirin Pamp <pamp@atix.de> - 0.0.5-1
- Update python-pulp-cli-deb to 0.0.5.

* Fri Sep 16 2022 Markus Bucher <bucher@atix.de> - 0.0.2-4
- Bumping release for better upgrade from 3.16 to 3.18

* Thu Sep 15 2022 Markus Bucher <bucher@atix.de> - 0.0.2-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.0.2-2
- Build against python 3.9

* Mon Dec 27 2021 Quirin Pamp <pamp@atix.de> - 0.0.2-1
- Release version 0.0.2.

* Fri Nov 05 2021 Maarten Beeckmans <maartenb@inuits.eu> - 0.0.1-1
- Initial package.
