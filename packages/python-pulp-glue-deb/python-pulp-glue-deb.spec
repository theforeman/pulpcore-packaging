%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global debug_package %{nil}

%global pypi_name pulp-glue-deb
%global srcname pulp_glue_deb

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Version agnostic glue library to talk to pulpcore's REST API. (deb plugin)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://pypi.org/project/pulp-glue-deb/
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
Requires:       python%{python3_pkgversion}-pulp-glue >= 0.23.2
Requires:       python%{python3_pkgversion}-pulp-glue < 0.28


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
%{python3_sitelib}/pulp_glue/deb
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
* Tue Aug 06 2024 Odilon Sousa <osousa@redhat.com> - 0.2.0-1
- Release python-pulp-glue-deb 0.2.0

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 0.1.0-1
- Release python-pulp-glue-deb 0.1.0

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 0.0.7-1
- Initial package.
