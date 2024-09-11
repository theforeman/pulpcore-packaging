%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name diff-match-patch

Name:           python-%{pypi_name}
Version:        20230430
Release:        1%{?dist}
Summary:        Repackaging of Google's Diff Match and Patch libraries

License:        Apache
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/diff_match_patch
%{python3_sitelib}/diff_match_patch-%{version}.dist-info/


%changelog
* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 20230430-1
- Update to 20230430

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 20200713-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 20200713-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 20200713-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20200713-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20200713-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 20200713-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov 20200713-1
- Update to 20200713

* Tue Apr 28 2020 Evgeni Golov - 20181111-1
- Initial package.
