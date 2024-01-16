%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-readonly-field

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        4%{?dist}
Summary:        Make Django model fields readonly

License:        MIT
URL:            https://github.com/peopledoc/django-readonly-field
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Force setuptools_scm usage for older setuptools
sed -i 's/setup()/setup(use_scm_version=True)/' setup.py


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_readonly_field
%{python3_sitelib}/tests
%{python3_sitelib}/django_readonly_field-%{version}-py%{python3_version}.egg-info
%exclude  %{python3_sitelib}/tests/


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.1.2-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.1.2-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.1.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 1.1.2-1
- Update to 1.1.2

* Thu Aug 11 2022 Odilon Sousa <osousa@redhat.com> - 1.1.1-3
- Update release for better upgrade from 3.16 to 3.18

* Tue Jul 26 2022 Odilon Sousa <osousa@redhat.com> - 1.1.1-1
- Release python-django-readonly-field 1.1.1

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.5-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.5-4
- Build against python 3.9

* Tue Oct 26 2021 Evgeni Golov - 1.0.5-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov - 1.0.5-2
- Build against Python 3.8

* Thu Jul 30 2020 Samir Jha - 1.0.5-1
- Initial package.
