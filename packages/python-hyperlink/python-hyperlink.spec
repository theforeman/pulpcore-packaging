%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name hyperlink

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        21.0.0
Release:        7%{?dist}
Summary:        A featureful, immutable, and correct URL for Python

License:        MIT
URL:            https://github.com/python-hyper/hyperlink
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-idna >= 2.5

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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jul 30 2026 Odilon Sousa <osousa@redhat.com> - 21.0.0-7
- Bump release for EL10 rebuild

* Wed Mar 26 2025 Odilon Sousa <osousa@redhat.com> - 21.0.0-6
- Rebuild against python3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 21.0.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 21.0.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 21.0.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 21.0.0-2
- Build against python 3.11

* Wed Jul 19 2023 Odilon Sousa <osousa@redhat.com> - 21.0.0-1
- Initial package.
