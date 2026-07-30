%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name s3transfer

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.19.0
Release:        2%{?dist}
Summary:        An Amazon S3 Transfer Manager

License:        Apache License 2.0
URL:            https://github.com/boto/s3transfer
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-botocore < 2.0a.0
Requires:       python%{python3_pkgversion}-botocore >= 1.37.4

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
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 0.19.0-2
- Bump release for EL10 rebuild

* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.19.0-1
- Update to 0.19.0

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.0-1
- Update to 0.18.0
- Update botocore minimum to >= 1.37.4 (upstream 0.18.0 requires botocore >= 1.37.4)

* Wed May 06 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.17.0-1
- Update to 0.17.0

* Sun Apr 26 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.16.1-1
- Update to 0.16.1

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.16.0-1
- Update to 0.16.0

* Sun Sep 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.14.0-1
- Update to 0.14.0

* Sun May 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.13.0-1
- Update to 0.13.0

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.12.0-1
- Update to 0.12.0

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
