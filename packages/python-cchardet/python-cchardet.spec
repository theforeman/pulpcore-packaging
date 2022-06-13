%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name cchardet

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.1.7
Release:        4%{?dist}
Summary:        cChardet is high speed universal character encoding detector

License:        Mozilla Public License
URL:            https://github.com/PyYoshi/cChardet
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

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
%doc README.rst src/ext/uchardet/README.md src/ext/uchardet/doc/README.maintainer
%exclude %{_bindir}/cchardetect
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 2.1.7-4
- Exclude files in bin for a better upgrade from python38 to python39 and removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 2.1.7-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.1.7-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 2.1.7-1
- Initial package.
