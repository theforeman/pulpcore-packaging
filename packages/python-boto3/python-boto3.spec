%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name boto3

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.38.23
Release:        2%{?dist}
Summary:        The AWS SDK for Python

License:        Apache License 2.0
URL:            https://github.com/boto/boto3
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-botocore >= %{version}
Requires:       python%{python3_pkgversion}-botocore < 1.39.0
Requires:       python%{python3_pkgversion}-jmespath < 2.0.0
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-s3transfer < 0.14.0
Requires:       python%{python3_pkgversion}-s3transfer >= 0.13.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
* Mon May 26 2025 Odilon Sousa <osousa@redhat.com> - 1.38.23-2
- Update requirements for s3transfer

* Sun May 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.23-1
- Update to 1.38.23

* Wed May 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.20-1
- Update to 1.38.20

* Sun May 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.18-1
- Update to 1.38.18

* Wed May 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.15-1
- Update to 1.38.15

* Sun May 11 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.13-1
- Update to 1.38.13

* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.10-1
- Update to 1.38.10

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.8-1
- Update to 1.38.8

* Wed Apr 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.5-1
- Update to 1.38.5

* Wed Apr 30 2025 Odilon Sousa <osousa@redhat.com> - 1.38.2-2
- Fix botocore and s3transfer requirements

* Fri Apr 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.38.2-1
- Update to 1.38.2

* Mon Mar 31 2025 Odilon Sousa <osousa@redhat.com> - 1.37.6-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.37.6-1
- Update to 1.37.6

* Fri Feb 28 2025 Odilon Sousa <osousa@redhat.com> - 1.37.2-2
- Update botocore requirements

* Wed Feb 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.37.2-1
- Update to 1.37.2

* Wed Feb 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.37.1-1
- Update to 1.37.1

* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.26-1
- Update to 1.36.26

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.21-1
- Update to 1.36.21

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.13-1
- Update to 1.36.13

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.8-1
- Update to 1.36.8

* Sun Jan 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.6-1
- Update to 1.36.6

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.3-1
- Update to 1.36.3

* Sun Jan 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.36.2-1
- Update to 1.36.2

* Wed Jan 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.99-1
- Update to 1.35.99

* Sun Jan 12 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.97-1
- Update to 1.35.97

* Fri Jan 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.96-1
- Update to 1.35.96

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.94-1
- Update to 1.35.94

* Mon Jan 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.92-1
- Update to 1.35.92

* Wed Dec 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.87-1
- Update to 1.35.87

* Sun Dec 22 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.86-1
- Update to 1.35.86

* Wed Dec 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.83-1
- Update to 1.35.83

* Mon Dec 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.81-1
- Update to 1.35.81

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.78-1
- Update to 1.35.78

* Sun Dec 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.71-1
- Update to 1.35.71

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.70-1
- Update to 1.35.70

* Wed Nov 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.65-1
- Update to 1.35.65

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.59-1
- Update to 1.35.59

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.54-1
- Update to 1.35.54

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.51-1
- Update to 1.35.51

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.35.49-1
- Update to 1.35.49

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
