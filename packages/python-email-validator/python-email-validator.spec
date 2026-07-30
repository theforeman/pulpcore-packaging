%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name email-validator
%global src_name email_validator

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.3.0
Release:        2%{?dist}
Summary:        A robust email address syntax and deliverability validation library

License:        Unlicense
URL:            https://github.com/JoshData/python-email-validator
Source0:        https://files.pythonhosted.org/packages/source/e/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-dnspython >= 2.0.0
Requires:       python%{python3_pkgversion}-idna >= 2.0.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/email_validator
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 2.3.0-2
- Bump release for EL10 rebuild

* Wed Apr 15 2026 Odilon Sousa <osousa@redhat.com> - 2.3.0-1
- Initial package.
