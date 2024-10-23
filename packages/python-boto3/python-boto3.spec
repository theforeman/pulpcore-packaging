%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name boto3

Name:           python-%{pypi_name}
Version:        1.35.46
Release:        1%{?dist}
Summary:        The AWS SDK for Python

License:        Apache License 2.0
URL:            https://github.com/boto/boto3
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-botocore >= %{version}
Requires:       python%{python3_pkgversion}-botocore < 1.36.0
Requires:       python%{python3_pkgversion}-jmespath < 2.0.0
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-s3transfer < 0.11.0
Requires:       python%{python3_pkgversion}-s3transfer >= 0.10.0


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.46-1
- Update to 1.35.46

* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.44-1
- Update to 1.35.44

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.18.35-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.18.35-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.18.35-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.18.35-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.18.35-3
- Build against python 3.9

* Wed Oct 27 2021 Evgeni Golov - 1.18.35-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 1.18.35-1
- Initial package.
