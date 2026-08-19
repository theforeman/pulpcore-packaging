%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name charset-normalizer
%global src_name charset_normalizer

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        3.5.1
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        https://files.pythonhosted.org/packages/source/c/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
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
%doc README.md
%exclude %{_bindir}/normalizer
%{python3_sitelib}/charset_normalizer
%{python3_sitelib}/charset_normalizer-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Aug 19 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.1-1
- Update to 3.5.1

* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 3.4.9-2
- Bump release for EL10 rebuild

* Wed Jul 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.9-1
- Update to 3.4.9

* Sun Apr 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.7-1
- Update to 3.4.7

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.6-1
- Update to 3.4.6

* Sun Mar 08 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.5-1
- Update to 3.4.5

* Wed Oct 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.4-1
- Update to 3.4.4

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.2-1
- Update to 3.4.2

* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 3.4.1-2
- Rebuild against python3.12

* Wed Dec 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.1-1
- Update to 3.4.1

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.0-1
- Update to 3.4.0

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.2-1
- Update to 3.3.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.1-5
- Remove SCL bits

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 2.1.1-4
- Dont obsolete python-charset-normalizer

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.1-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 2.1.1-1
- Update to 2.1.1

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-4
- Exclude files in bin for a better upgrade from python38 to python39 and removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.11-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.0.11-1
- Release python-charset-normalizer 2.0.11

* Mon Nov 01 2021 Odilon Sousa - 2.0.7-1
- Initial package.
