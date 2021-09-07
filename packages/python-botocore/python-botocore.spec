%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name botocore

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.21.35
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        Apache License 2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dateutil < 3.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dateutil >= 2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jmespath < 1.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 < 1.27
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.25.4


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt tests/unit/auth/aws4_testsuite/LICENSE
%doc README.rst docs/README.md tests/unit/auth/aws4_testsuite/post-sts-token/readme.txt tests/unit/response_parsing/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Sep 03 2021 Evgeni Golov - 1.21.35-1
- Initial package.
