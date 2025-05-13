%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-glue

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.32.3
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

Requires:       python%{python3_pkgversion}-packaging < 25
Requires:       python%{python3_pkgversion}-packaging >= 20.0
Requires:       python%{python3_pkgversion}-requests < 2.33
Requires:       python%{python3_pkgversion}-requests >= 2.24.0

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
%{python3_sitelib}/pulp_glue
%{python3_sitelib}/pulp_glue-%{version}.dist-info/


%changelog
* Tue May 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.32.3-1
- Update to 0.32.3

* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.32.1-1
- Update to 0.32.1

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.31.1-3
- Add obsoletes for python3.11 package

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 0.31.1-2
- Rebuild against python3.12

* Tue Mar 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.31.1-1
- Update to 0.31.1

* Fri Feb 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.31.0-1
- Update to 0.31.0

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.30.2-1
- Update to 0.30.2

* Wed Oct 09 2024 Odilon Sousa <osousa@redhat.com> - 0.29.2-2
- Update requirement for requests

* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.29.2-1
- Update to 0.29.2

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.28.4-1
- Update to 0.28.4

* Fri Aug 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.27.2-1
- Update to 0.27.2

* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 0.27.1-1
- Release python-pulp-glue 0.27.1

* Tue Jun 18 2024 Odilon Sousa <osousa@redhat.com> - 0.25.6-1
- Release python-pulp-glue 0.25.6

* Mon Jun 10 2024 Odilon Sousa <osousa@redhat.com> - 0.25.4-1
- Release python-pulp-glue 0.25.4

* Mon Jun 03 2024 Evgeni Golov - 0.25.3-1
- Release python-pulp-glue 0.25.3

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
