%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name beautifulsoup4

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.11.1
Release:        1%{?dist}
Summary:        Screen-scraping library

License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-soupsieve > 1.2


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
%license LICENSE COPYING.txt
%doc README.md
%{python3_sitelib}/bs4
%{python3_sitelib}/bs4/builder
%{python3_sitelib}/bs4/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 20 2022 Odilon Sousa 4.11.1-1
- Update to 4.11.1

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.10.0-2
- Build against python 3.9

* Mon Feb 21 2022 Odilon Sousa <osousa@redhat.com> - 4.10.0-1
- Initial package.
