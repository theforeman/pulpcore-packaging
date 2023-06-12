%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name Django
%global srcname django

Name:           %{?scl_prefix}python-%{srcname}
Version:        3.2.19
Release:        1%{?dist}
Summary:        A high-level Python Web framework that encourages rapid development and clean, pragmatic design

License:        BSD-3-Clause
URL:            https://www.djangoproject.com/
Source0:        https://files.pythonhosted.org/packages/source/D/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Fixed-28401-Allow-hashlib.md5-calls-to-work-with-FIP.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asgiref < 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asgiref >= 3.3.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytz
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sqlparse >= 0.2.2
%if 0%{?!scl:1}
Obsoletes:      python3-%{srcname} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{srcname} < %{version}-%{release}
%endif


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version} -p 1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# hard-code python3 in django-admin
pushd django
for file in bin/django-admin.py conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE LICENSE.python django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md django/contrib/admin/static/admin/fonts/LICENSE.txt django/contrib/admin/static/admin/img/LICENSE django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt django/contrib/gis/gdal/LICENSE django/contrib/gis/geos/LICENSE django/dispatch/license.txt docs/_theme/djangodocs/static/fontawesome/LICENSE.txt
%doc README.rst django/contrib/admin/static/admin/fonts/README.txt django/contrib/admin/static/admin/img/README.txt docs/README.rst docs/_theme/djangodocs/static/fontawesome/README.md extras/README.TXT tests/README.rst
%{_bindir}/django-admin
%exclude %{_bindir}/django-admin.py
%{python3_sitelib}/django
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jun 12 2023 Odilon Sousa <osousa@redhat.com> - 3.2.19-1
- Release python-django 3.2.19

* Thu Mar 02 2023 Odilon Sousa <osousa@redhat.com> - 3.2.18-1
- Update python-django to 3.2.18 to fix CVE-2023-24580

* Fri Feb 03 2023 Odilon Sousa 3.2.17-1
- Update to 3.2.17

* Tue Jan 24 2023 Odilon Sousa <osousa@redhat.com> - 3.2.16-1
- Release python-django 3.2.16

* Tue Sep 20 2022 Odilon Sousa 3.2.15-1
- Update to 3.2.15

* Thu May 12 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.13-4
- Fix obsolete named package

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.13-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 29 2022 Odilon Sousa <osousa@redhat.com> - 3.2.13-2
- Rebuilding against python39

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 3.2.13-1
- Release python-django 3.2.13

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 3.2.12-2
- Rebuild against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 3.2.12-1
- Release python-django 3.2.12

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.2.9-1
- Release python-django 3.2.9

* Tue Oct 19 2021 Evgeni Golov - 3.2.7-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 15 2021 Matthias Dellweg 3.2.7-3
- Add a patch for FIPS compliency.

* Fri Sep 10 2021 Evgeni Golov 3.2.7-2
- Exclude django-admin.py again, we never shipped that.

* Wed Sep 08 2021 Evgeni Golov 3.2.7-1
- Update to 3.2.7

* Wed Sep 08 2021 Evgeni Golov - 2.2.24-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 2.2.24-1
- Update to 2.2.24

* Mon May 31 2021 Evgeni Golov - 2.2.23-1
- Release python-django 2.2.23

* Tue Apr 06 2021 Evgeni Golov - 2.2.20-1
- Release python-django 2.2.20

* Fri Mar 19 2021 Evgeni Golov 2.2.19-1
- Update to 2.2.19

* Mon Nov 02 2020 Evgeni Golov 2.2.17-1
- Update to 2.2.17

* Thu Sep 10 2020 Matthias Dellweg 2.2.16-2
- Add a patch to support running in a FIPS environment

* Tue Sep 01 2020 Evgeni Golov 2.2.16-1
- Update to 2.2.16

* Mon Aug 10 2020 Evgeni Golov 2.2.15-1
- Update to 2.2.15

* Mon Jul 20 2020 Evgeni Golov 2.2.14-1
- Update to 2.2.14

* Thu Jun 04 2020 Evgeni Golov 2.2.13-1
- Update to 2.2.13

* Tue Apr 14 2020 Evgeni Golov 2.2.12-1
- Update to 2.2.12

* Wed Mar 18 2020 Samir Jha 2.2.11-1
- Update to 2.2.11

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.10-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov - 2.2.10-1
- Release python-django 2.2.10

* Wed Dec 18 2019 Evgeni Golov 2.2.9-1
- Update to 2.2.9

* Fri Dec 13 2019 Evgeni Golov 2.2.8-1
- Update to 2.2.8

* Mon Nov 18 2019 Evgeni Golov - 2.2.7-1
- Initial package.
