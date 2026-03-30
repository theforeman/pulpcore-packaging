%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name fastjsonschema

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.21.2
Release:        1%{?dist}
Summary:        Fast JSON schema validator for Python.

License:        BSD 3-Clause "New" or "Revised" License
URL:            https://github.com/horejsek/python-fastjsonschema
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

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
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Mar 30 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.21.2-1
- Update to 2.21.2

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 2.21.1-2
- Rebuild against python3.12

* Tue Feb 18 2025 Odilon Sousa <osousa@redhat.com> - 2.21.1-1
- Initial package.
