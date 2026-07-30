%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name subprocess-tee
%global src_name subprocess_tee

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.2
Release:        2%{?dist}
Summary:        A subprocess.run alternative that also allows capturing combined stdout/stderr

License:        MIT
URL:            https://github.com/pycontribs/subprocess-tee
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm >= 7.0.0
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.4.2-2
- Bump release for EL10 rebuild

* Fri Jun 12 2026 Odilon Sousa <osousa@redhat.com> - 0.4.2-1
- Initial package
