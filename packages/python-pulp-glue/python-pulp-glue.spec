%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-glue

Name:           python-%{pypi_name}
Version:        0.25.1
Release:        1%{?dist}
Summary:        Version agnostic glue library to talk to pulpcore's REST API

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
Requires:       python%{python3_pkgversion}-packaging < 25
Requires:       python%{python3_pkgversion}-packaging >= 20.0
Requires:       python%{python3_pkgversion}-requests < 2.32
Requires:       python%{python3_pkgversion}-requests >= 2.24.0
Conflicts:      python%{python3_pkgversion}-requests >= 2.32
Requires:       python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

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
%{python3_sitelib}/pulp_glue
%{python3_sitelib}/pulp_glue-%{version}.dist-info/


%changelog
* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 0.25.1-1
- Release python-pulp-glue 0.25.1

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 0.23.2-1
- Release python-pulp-glue 0.23.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.21.2-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.21.2-3
- Obsolete python39 packages for a smooth upgrade

* Wed Nov 15 2023 Patrick Creech <pcreech@redhat.com> - 0.21.2-2
- Rebuild for python 3.11

* Thu Sep 14 2023 Quirin Pamp <pamp@atix.de> - 0.21.2-1
- Update python-pulp-glue to 0.21.2.

* Wed Aug 09 2023 Odilon Sousa <osousa@redhat.com> - 0.19.2-2
- Update python-requests requirement

* Wed Jul 05 2023 Odilon Sousa - 0.19.2-1
- Initial package.
