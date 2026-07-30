%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name pydantic

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.13.4
Release:        2%{?dist}
Summary:        Data validation using Python type hints

License:        MIT
URL:            https://github.com/pydantic/pydantic/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_fancy_pypi_readme >= 22.5.0

Requires:  python%{python3_pkgversion}-typing-extensions >= 4.14.1
Requires:  python%{python3_pkgversion}-annotated-types >= 0.6.0
Requires:  python%{python3_pkgversion}-pydantic-core == 2.46.4
Requires:  python%{python3_pkgversion}-typing-inspection >= 0.4.2

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%package -n python%{python3_pkgversion}-%{pypi_name}+email
Summary:        Metapackage for python%{python3_pkgversion}-pydantic: email extra
Requires:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-email-validator

%description -n python%{python3_pkgversion}-%{pypi_name}+email
This is a metapackage bringing in email extra requires for
python%{python3_pkgversion}-%{pypi_name}.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-%{pypi_name}+email
%ghost %{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.13.4-2
- Bump release for EL10 rebuild

* Wed May 13 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.13.4-1
- Update to 2.13.4
- Update pydantic-core requirement to 2.46.4
- Update typing-extensions lower bound to >= 4.14.1, typing-inspection to >= 0.4.2

* Mon Apr 27 2026 Odilon Sousa <osousa@redhat.com> - 2.13.3-2
- Update pydantic-core requirement to 2.46.3

* Wed Apr 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.13.3-1
- Update to 2.13.3

* Wed Apr 15 2026 Odilon Sousa <osousa@redhat.com> - 2.13.0-2
- Update pydantic-core requirement to 2.46.0

* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.13.0-1
- Update to 2.13.0
- Add +email metapackage for pydantic[email] extra (requires email-validator)

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.12.5-1
- Update to 2.12.5
- Update pydantic-core requirement to 2.41.5

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.11.2-1
- Release python-pydantic 2.11.2

* Thu Apr 03 2025 Odilon Sousa <osousa@redhat.com> - 2.11.1-1
- Initial Release

