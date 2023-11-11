%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name odfpy

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.4.1
Release:        7%{?dist}
Summary:        Python API and tools to manipulate OpenDocument files

License:        GPLv2+ or Apache-2.0
URL:            https://github.com/eea/odfpy
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-defusedxml


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
%license APACHE-LICENSE-2.0.txt GPL-LICENSE-2.txt
%doc contrib/ODFFile/README.txt README.md
%exclude %{_bindir}/csv2ods
%exclude %{_bindir}/mailodf
%exclude %{_bindir}/odf2mht
%exclude %{_bindir}/odf2xhtml
%exclude %{_bindir}/odf2xml
%exclude %{_bindir}/odfimgimport
%exclude %{_bindir}/odflint
%exclude %{_bindir}/odfmeta
%exclude %{_bindir}/odfoutline
%exclude %{_bindir}/odfuserfield
%exclude %{_bindir}/xml2odf
%{_mandir}/*/csv2ods*
%{_mandir}/*/mailodf*
%{_mandir}/*/odf2mht*
%{_mandir}/*/odf2xhtml*
%{_mandir}/*/odf2xml*
%{_mandir}/*/odfimgimport*
%{_mandir}/*/odflint*
%{_mandir}/*/odfmeta*
%{_mandir}/*/odfoutline*
%{_mandir}/*/odfuserfield*
%{_mandir}/*/xml2odf*
%{python3_sitelib}/odf
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.4.1-7
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.4.1-6
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 1.4.1-5
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 1.4.1-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 1.4.1-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.4.1-2
- Fix License tag in spec file

* Tue Apr 28 2020 Evgeni Golov - 1.4.1-1
- Initial package.
