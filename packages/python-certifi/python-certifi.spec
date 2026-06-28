%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name certifi

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2026.6.17
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         certifi-2025.07.14-use-system-cert.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  ca-certificates

Requires:       ca-certificates

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled Root Certificates collection
rm -rf certifi/*.pem


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install
%pyproject_save_files certifi

	
%check
set -ex
# sanity check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
test $(%{__python3} -m certifi) == /etc/pki/tls/certs/ca-bundle.crt
test $(%{__python3} -c 'import certifi; print(certifi.where())') == /etc/pki/tls/certs/ca-bundle.crt
%{__python3} -c 'import certifi; print(certifi.contents())' > contents
diff --ignore-blank-lines /etc/pki/tls/certs/ca-bundle.crt contents


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Sun Jun 28 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2026.6.17-1
- Update to 2026.6.17

* Wed Jun 10 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2026.5.20-1
- Update to 2026.5.20

* Sun Apr 26 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2026.4.22-1
- Update to 2026.4.22

* Sun Mar 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2026.2.25-1
- Update to 2026.2.25

* Sun Jan 18 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2026.1.4-1
- Update to 2026.1.4

* Sun Nov 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.11.12-1
- Update to 2025.11.12

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.10.5-1
- Update to 2025.10.5

* Wed Aug 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.8.3-1
- Update to 2025.8.3

* Wed Jul 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.7.14-1
- Update to 2025.7.14

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.4.26-1
- Update to 2025.4.26

* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 2025.1.31-2
- Rebuild against python3.12

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2025.1.31-1
- Update to 2025.1.31

* Wed Dec 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2024.12.14-1
- Update to 2024.12.14

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2022.12.7-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2022.12.7-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2022.12.7-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2022.12.7-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2022.12.7-1
- Update to 2022.12.7

* Tue Apr 26 2022 Yanis Guenane - 2020.6.20-3
- Build against Python 3.9

* Wed Sep 08 2021 Evgeni Golov - 2020.6.20-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov - 2020.6.20-1
- Initial package.
