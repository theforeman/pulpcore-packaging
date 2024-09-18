%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-guid
%global src_name django_guid

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs

License:        BSD
URL:            https://github.com/snok/django-guid
Source0:        https://files.pythonhosted.org/packages/source/d/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-django < 5.0.0
Requires:       python%{python3_pkgversion}-django >= 3.1.1

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{src_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{src_name}
%exclude %{python3_sitelib}/CHANGELOG.rst
%{python3_sitelib}/%{src_name}-%{version}.dist-info/


%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.0-1
- Update to 3.4.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 3.3.0-5
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-4
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-3
- Build against python 3.11

* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 3.3.0-2
- Update django requirement

* Tue Sep 20 2022 Odilon Sousa 3.3.0-1
- Update to 3.3.0

* Tue May 24 2022 Odilon Sousa <osousa@redhat.com> - 3.2.2-1
- Release python-django-guid 3.2.2

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.1-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.2.1-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 3.2.1-1
- Release python-django-guid 3.2.1

* Tue Oct 19 2021 Evgeni Golov - 3.2.0-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 3.2.0-1
- Update to 3.2.0

* Wed Sep 08 2021 Evgeni Golov - 2.2.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Jan 18 2021 Evgeni Golov - 2.2.0-1
- Initial package.
