%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name bracex

Name:           python-%{pypi_name}
Version:        2.5
Release:        1%{?dist}
Summary:        Bash style brace expander

License:        MIT License
URL:            https://github.com/facelessuser/bracex
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling >= 0.21.1
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.5-1
- Update to 2.5

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.2.1-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.2.1-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.2.1-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.2.1-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.2.1-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa 2.2.1-1
- Update to 2.2.1

* Wed Nov 03 2021 Odilon Sousa 2.2-1
- Update to 2.2

* Mon Sep 06 2021 Evgeni Golov - 2.1.1-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov - 2.1.1-1
- Initial package.
