%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%global debug_package %{nil}

%global pypi_name pulp-glue-deb
%global srcname pulp_glue_deb

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.3.3
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

Requires:       python%{python3_pkgversion}-pulp-glue >= 0.23.2
Requires:       python%{python3_pkgversion}-pulp-glue < 0.33

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
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
* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.3-1
- Update to 0.3.3

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.3.2-3
- Add obsoletes for python3.11 package

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 0.3.2-2
- Rebuild against python3.12

* Thu Feb 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.2-1
- Update to 0.3.2

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.1-1
- Update to 0.3.1

* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.0-1
- Update to 0.3.0

* Tue Aug 06 2024 Odilon Sousa <osousa@redhat.com> - 0.2.0-1
- Release python-pulp-glue-deb 0.2.0

* Fri May 17 2024 Odilon Sousa <osousa@redhat.com> - 0.1.0-1
- Release python-pulp-glue-deb 0.1.0

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 0.0.7-1
- Initial package.
