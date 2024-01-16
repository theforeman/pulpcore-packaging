%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name botocore

Name:           python-%{pypi_name}
Version:        1.21.35
Release:        9%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        Apache License 2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if 0%{?rhel} == 9 && "%{?python3_pkgversion}" != "3.11"
Requires:       python%{python3_pkgversion}-dateutil < 1:3.0.0
Requires:       python%{python3_pkgversion}-dateutil >= 1:2.1
%else
Requires:       python%{python3_pkgversion}-dateutil < 3.0.0
Requires:       python%{python3_pkgversion}-dateutil >= 2.1
%endif
Requires:       python%{python3_pkgversion}-jmespath < 1.0.0
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-urllib3 < 1.27
Requires:       python%{python3_pkgversion}-urllib3 >= 1.25.4


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt tests/unit/auth/aws4_testsuite/LICENSE
%doc README.rst docs/README.md tests/unit/auth/aws4_testsuite/post-sts-token/readme.txt tests/unit/response_parsing/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.21.35-9
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.21.35-8
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.21.35-7
- Add python39 obsoletes to package

* Wed Nov 15 2023 Patrick Creech <pcreech@redhat.com> - 1.21.35-6
- Don't use epoch for dateutil dependency if we aren't using system python

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.21.35-5
- Build against python 3.11

* Thu May 12 2022 Satoe Imaishi <simaishi@redhat.com> - 1.21.35-4
- Add epoch for python-dateutil requires for el9

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.21.35-3
- Build against python 3.9

* Wed Oct 27 2021 Evgeni Golov - 1.21.35-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 1.21.35-1
- Initial package.
