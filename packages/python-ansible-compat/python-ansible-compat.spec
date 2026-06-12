%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name ansible-compat
%global src_name ansible_compat

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        4.1.11
Release:        1%{?dist}
Summary:        Ansible compatibility goodies

License:        MIT
URL:            https://github.com/ansible/ansible-compat
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 7.0.5
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

Requires:       python%{python3_pkgversion}-jsonschema >= 4.6.0
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-subprocess-tee >= 0.4.1

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Fri Jun 12 2026 Odilon Sousa <osousa@redhat.com> - 4.1.11-1
- Initial package
