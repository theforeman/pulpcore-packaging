%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name trove-classifiers
%global src_name trove_classifiers

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2025.3.13.13
Release:        2%{?dist}
Summary:        Canonical source for classifiers on PyPI (pypi.org)
License:        None
URL:            https://github.com/pypa/trove-classifiers
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-calver
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
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
%doc README.md
%{python3_sitelib}/trove_classifiers
%{python3_sitelib}/trove_classifiers-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 2025.3.13.13-2
- Rebuild against python3.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.3.13.13-1
- Update to 2025.3.13.13

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.3.3.18-1
- Update to 2025.3.3.18

* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.2.18.16-1
- Update to 2025.2.18.16

* Tue Sep 17 2024 Odilon Sousa <osousa@redhat.com> - 2024.9.12-1
- Release python-trove-classifiers 2024.9.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2023.7.6-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2023.7.6-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2023.7.6-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2023.7.6-2
- Build against python 3.11

* Tue Jul 18 2023 Odilon Sousa <osousa@redhat.com> - 2023.7.6-1
- Initial package.
