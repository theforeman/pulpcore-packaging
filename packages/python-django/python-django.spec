%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name Django
%global srcname django

Name:           python-%{srcname}
Version:        4.2.14
Release:        1%{?dist}
Summary:        A high-level Python web framework that encourages rapid development and clean, pragmatic design

License:        BSD-3-Clause
URL:            https://www.djangoproject.com/
Source0:        https://files.pythonhosted.org/packages/source/D/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-asgiref < 4
Requires:       python%{python3_pkgversion}-asgiref >= 3.3.2
Requires:       python%{python3_pkgversion}-pytz
Requires:       python%{python3_pkgversion}-sqlparse >= 0.2.2
%if 0%{?!scl:1}
Obsoletes:      python3-%{srcname} < %{version}-%{release}
%endif
%if 0%{?rhel} == 8
Obsoletes:      python38-%{srcname} < %{version}-%{release}
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# hard-code python3 in django-admin
pushd django
for file in conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE LICENSE.python django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md django/contrib/admin/static/admin/img/LICENSE django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt django/contrib/gis/gdal/LICENSE django/contrib/gis/geos/LICENSE django/dispatch/license.txt docs/_theme/djangodocs/static/fontawesome/LICENSE.txt
%doc README.rst django/contrib/admin/static/admin/img/README.txt docs/README.rst docs/_theme/djangodocs/static/fontawesome/README.md extras/README.TXT tests/README.rst
%{_bindir}/django-admin
%{python3_sitelib}/django
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Aug 01 2024 Odilon Sousa <osousa@redhat.com> - 4.2.14-1
- Release python-django 4.2.14

* Thu Mar 14 2024 Odilon Sousa <osousa@redhat.com> - 4.2.11-1
- Release python-django 4.2.11

* Mon Jan 29 2024 Odilon Sousa <osousa@redhat.com> - 4.2.9-1
- Release python-django 4.2.9

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 4.2.2-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.2.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.2.2-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa 4.2.2-1
- Update to 4.2.2

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
