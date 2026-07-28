%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pkginfo

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.12.1.2
Release:        4%{?dist}
Summary:        Query metadatdata from sdists / bdists / installed packages

License:        MIT
URL:            https://code.launchpad.net/~tseaver/pkginfo/trunk
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


Requires:       python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

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
%doc docs/examples/mypackage-0.1/README.txt README.txt
%{_bindir}/pkginfo
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 1.12.1.2-4
- Bump release for EL10 rebuild

* Wed Apr 09 2025 Odilon Sousa <osousa@redhat.com> - 1.12.1.2-3
- Add obsoletes for python3.11 package

* Mon Mar 24 2025 Odilon Sousa <osousa@redhat.com> - 1.12.1.2-2
- Rebuild against python3.12

* Wed Feb 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.12.1.2-1
- Update to 1.12.1.2

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.11.3-1
- Update to 1.11.3

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.11.2-1
- Update to 1.11.2

* Tue Sep 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.11.1-1
- Update to 1.11.1

* Mon Sep 09 2024 Odilon Sousa <osousa@redhat.com> - 1.11.0-1
- Release python-pkginfo 1.11.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.9.6-4
- Remove SCL bits

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.9.6-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.9.6-2
- Build against python 3.11

* Mon Aug 07 2023 Odilon Sousa <osousa@redhat.com> - 1.9.6-1
- Release python-pkginfo 1.9.6

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 1.8.2-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.8.2-2
- Build against python 3.9

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 1.8.2-1
- Release python-pkginfo 1.8.2

* Tue Oct 26 2021 Evgeni Golov - 1.7.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 1.7.1-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 1.7.1-1
- Initial package.
