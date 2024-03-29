%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name tomli_w

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        5%{?dist}
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project2/tomli-w/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  pyproject-rpm-macros

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
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.0.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-2
- Build against python 3.11

* Thu Jul 13 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-1
- Initial package
