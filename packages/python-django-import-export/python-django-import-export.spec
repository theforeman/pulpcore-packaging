%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?python_disable_dependency_generator}

# Created by pyp2rpm-3.3.3
%global pypi_name django-import-export
%global src_name django_import_export

Name:           python-%{pypi_name}
Version:        3.3.9
Release:        1%{?dist}
Summary:        Django application and library for importing and exporting data with included admin integration

License:        BSD License
URL:            https://github.com/django-import-export/django-import-export
Source0:        https://files.pythonhosted.org/packages/source/d/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django >= 3.2
Requires:       python%{python3_pkgversion}-diff-match-patch
Requires:       python%{python3_pkgversion}-tablib >= 3.2.1

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/import_export
%{python3_sitelib}/django_import_export-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.9-1
- Update to 3.3.9

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.1.0-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.1.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.1.0-2
- Build against python 3.11

* Mon Oct 02 2023 Odilon Sousa <osousa@redhat.com> - 3.1.0-1
- Release python-django-import-export 3.1.0

* Fri Feb 03 2023 Odilon Sousa 3.0.2-1
- Update to 3.0.2

* Tue Sep 20 2022 Odilon Sousa 2.8.0-1
- Update to 2.8.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 2.7.1-6
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri May 06 2022 Odilon Sousa <osousa@redhat.com> - 2.7.1-5
- Rebuilding with python_disable_dependency_generator macro

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.7.1-4
- Build against python 3.9

* Thu Mar 03 2022 Odilon Sousa <osousa@redhat.com> - 2.7.1-3
- Add obsolete again for smooth upgrade 

* Mon Feb 14 2022 Patrick Creech <pcreech@redhat.com> - 2.7.1-2
- fixup dependency issues

* Mon Feb 07 2022 Odilon Sousa 2.7.1-1
- Update to 2.7.1

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 2.6.1-1
- Release python-django-import-export 2.6.1

* Tue Oct 19 2021 Evgeni Golov - 2.5.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 2.5.0-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.5.0-1
- Update to 2.5.0

* Mon Nov 02 2020 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Tue Aug 25 2020 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Tue Apr 28 2020 Evgeni Golov - 2.0.2-1
- Initial package.
