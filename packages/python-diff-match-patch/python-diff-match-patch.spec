%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name diff-match-patch

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        20200713
Release:        5%{?dist}
Summary:        Repackaging of Google's Diff Match and Patch libraries

License:        Apache
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 38.6.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


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
%doc README.md
%{python3_sitelib}/diff_match_patch
%{python3_sitelib}/diff_match_patch-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 20200713-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20200713-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20200713-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 20200713-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov 20200713-1
- Update to 20200713

* Tue Apr 28 2020 Evgeni Golov - 20181111-1
- Initial package.
