%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name frozenlist

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.8.0
Release:        2%{?dist}
Summary:        A list-like structure which implements collections

License:        Apache 2
URL:            https://github.com/aio-libs/frozenlist
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Downstream-only-Build-normal-wheels-in-place.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-expandvars
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version} -p1


%build
set -ex
export FROZENLIST_NO_EXTENSIONS=1
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Jul 27 2026 Odilon Sousa <osousa@redhat.com> - 1.8.0-2
- Bump release for EL10 rebuild

* Wed Apr 01 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.0-1
- Update to 1.8.0
- Build pure Python; frozenlist 1.8.0 requires Cython 3 for C extension

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 1.5.0-2
- Rebuild against python3.12

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.0-1
- Update to 1.5.0

* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.1-1
- Update to 1.4.1

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.3.3-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.3.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.3.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.3.3-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.3.3-1
- Update to 1.3.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.3.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa - 1.3.0-1
- Initial package.
