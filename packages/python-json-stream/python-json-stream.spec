%global debug_package %{nil}

%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12
%global pypi_name json-stream
%global pkg_name json_stream

Name:           python%{python3_pkgversion}-%{pkg_name}
Version:        2.4.1
Release:        1%{?dist}
Summary:        Streaming JSON encoder and decoder

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/daggaz/json-stream
Source:         https://files.pythonhosted.org/packages/source/j/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-json_stream_rs_tokenizer >= 0.4.17

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pkg_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/
%{python3_sitelib}/%{pkg_name}/

%changelog
* Wed Apr 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.1-1
- Update to 2.4.1

* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.4-1
- Update to 2.3.4

* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 2.3.3-2
- Rebuild against python3.12

* Sun Jan 12 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.3-1
- Update to 2.3.3

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.3.2-4
- Rollback overzealous obsoletes

* Wed Nov 29 2023 Odilon Sousa <osousa@redhat.com> - 2.3.2-3
- Add {?dist} to python-json-stream

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.3.2-2
- Add python39 obsoletes to package

* Mon Nov 13 2023 Odilon Sousa <osousa@redhat.com> - 2.3.2-1
- Initial package.