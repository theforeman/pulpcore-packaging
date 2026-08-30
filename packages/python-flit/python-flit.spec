%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name flit

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.0.2
Release:        1%{?dist}
Summary:        Distribution-building parts of Flit. See flit package for more information

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://pypi.org/project/flit-core/
Source:         https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core >= %{version}

Requires:       python%{python3_pkgversion}-tomli_w
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-flit_core >= %{version}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/flit

%changelog
* Sun Aug 30 04:26:30 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.2-1
- Update to 4.0.2
- Remove unsatisfiable flit_core < 4 upper bound (flit 4.0.2 requires flit_core >= 4.0.2)

* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 3.12.0-2
- Bump release for EL10 rebuild

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2025 Odilon Sousa <osousa@redhat.com> - 3.11.0-2
- Rebuild against python3.12

* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.11.0-1
- Update to 3.11.0

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.10.1-1
- Update to 3.10.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.9.0-6
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.9.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-4
- Build against python 3.11

* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-3
- Fix tomli_w requirement

* Thu Jul 20 2023 Odilon Sousa <osousa@redhat.com> - 3.9.0-2
- Add package requirements

* Fri Jul 14 2023 Odilon Sousa - 3.9.0-1
- Initial package.
