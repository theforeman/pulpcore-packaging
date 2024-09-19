%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.7
%global pypi_name soupsieve

Name:           python-%{pypi_name}
Version:        2.6
Release:        1%{?dist}
Summary:        A modern CSS selector implementation for Beautiful Soup

License:        MIT License
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
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
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.6-1
- Update to 2.6

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.3.1-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.3.1-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.3.1-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.3.1-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.3.1-3
- Build against python 3.9

* Tue Feb 22 2022 Odilon Sousa <osousa@redhat.com> - 2.3.1-2
- Release python-soupsieve 2.3.1

* Mon Feb 21 2022 Odilon Sousa <osousa@redhat.com> - 2.3.1-1
- Initial package.
