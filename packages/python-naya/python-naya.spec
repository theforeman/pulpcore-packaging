%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.8
%global pypi_name naya

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1.1
Release:        4%{?dist}
Summary:        A fast streaming JSON parser written in pure python

License:        MIT
URL:            https://github.com/danielyule/naya
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python38-%{pypi_name} < %{version}-%{release}
%endif

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.1.1-4
- Build against python 3.11

* Wed May 25 2022 Odilon Sousa <osousa@redhat.com> - 1.1.1-3
- Bump release to rebuild against python 3.9

* Tue May 24 2022 Odilon Sousa <osousa@redhat.com> - 1.1.1-2
- Bump package release for a rebuild on python 3.9

* Thu May 19 2022 Odilon Sousa <osousa@redhat.com> - 1.1.1-1
- Initial package.
