%global debug_package %{nil}

%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12


# Created by pyp2rpm-3.3.8
%global pypi_name json-stream-rs-tokenizer
%global pkg_name json_stream_rs_tokenizer

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.4.28
Release:        2%{?dist}
Summary:        Faster tokenizer for the json-stream Python library

License:        MIT
URL:            https://github.com/smheidrich/py-json-stream-rs-tokenizer
Source0:        https://files.pythonhosted.org/packages/source/j/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pkg_name}-%{version}
# Remove bundled egg-info
rm -rf %{pkg_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pkg_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pkg_name}/


%changelog
* Tue Apr 01 2025 Odilon Sousa <osousa@redhat.com>
- Rebuild against pyton3.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.28-1
- Update to 0.4.28

* Fri Jan 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.27-1
- Update to 0.4.27

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.4.26-1
- Update to 0.4.26

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.4.25-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.4.25-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.4.25-2
- Add python39 obsoletes to package

* Mon Nov 13 2023 Odilon Sousa <osousa@redhat.com> - 0.4.25-1
- Initial package.
