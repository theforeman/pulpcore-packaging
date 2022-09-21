%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name charset-normalizer

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.1.1
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

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
%license LICENSE
%doc README.md
%exclude %{_bindir}/normalizer
%{python3_sitelib}/charset_normalizer
%{python3_sitelib}/charset_normalizer-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 20 2022 Odilon Sousa 2.1.1-1
- Update to 2.1.1

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-4
- Exclude files in bin for a better upgrade from python38 to python39 and removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.11-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-1
- Release python-charset-normalizer 2.0.11

* Mon Nov 01 2021 Odilon Sousa - 2.0.7-1
- Initial package.
