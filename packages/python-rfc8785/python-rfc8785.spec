%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name rfc8785

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.1.4
Release:        2%{?dist}
Summary:        JSON Canonicalization Scheme (JCS) implementation per RFC 8785

License:        Apache-2.0
URL:            https://github.com/nicowillis/rfc8785
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit-core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.1.4-2
- Bump release for EL10 rebuild

* Tue Apr 14 2026 Odilon Sousa <osousa@redhat.com> - 0.1.4-1
- Initial package.
