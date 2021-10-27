%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name boto3

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.18.35
Release:        2%{?dist}
Summary:        The AWS SDK for Python

License:        Apache License 2.0
URL:            https://github.com/boto/boto3
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-botocore < 1.22.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-botocore < 2.0a0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-botocore >= 1.21.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-botocore >= 1.21.35
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jmespath < 1.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-s3transfer < 0.6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-s3transfer >= 0.5.0


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 27 2021 Evgeni Golov - 1.18.35-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 1.18.35-1
- Initial package.
