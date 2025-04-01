%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name s3transfer

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.11.2
Release:        2%{?dist}
Summary:        An Amazon S3 Transfer Manager

License:        Apache License 2.0
URL:            https://github.com/boto/s3transfer
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-botocore < 2.0a.0
Requires:       python%{python3_pkgversion}-botocore >= 1.36.0

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com> - 0.11.2-2
- Rebuild against python3.12

* Mon Jan 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.2-1
- Update to 0.11.2

* Sun Jan 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.1-1
- Update to 0.11.1

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.4-1
- Update to 0.10.4

* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.3-1
- Update to 0.10.3

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.5.0-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.5.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.5.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.5.0-3
- Build against python 3.9

* Wed Oct 27 2021 Evgeni Golov - 0.5.0-2
- Rebuild against Python 3.8

* Fri Sep 03 2021 Evgeni Golov - 0.5.0-1
- Initial package.
