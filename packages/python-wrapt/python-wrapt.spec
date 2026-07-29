%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name wrapt

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.17.3
Release:        2%{?dist}
Summary:        Module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 38.3.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 1.17.3-2
- Bump release for EL10 rebuild

* Sun Sep 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.3-1
- Update to 1.17.3

* Wed Apr 02 2025 Odilon Sousa <osousa@redhat.com> - 1.17.2-2
- Rebuild against python3.12

* Wed Jan 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.2-1
- Update to 1.17.2

* Sun Jan 12 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.1-1
- Update to 1.17.1

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.0-1
- Update to 1.17.0

* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.16.0-1
- Update to 1.16.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.14.1-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.14.1-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.14.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.14.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa - 1.14.1-1
- Initial package.
