%global python3_pkgversion 3.12
%global __python3 %{_bindir}/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name docutils

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.22.3
Release:        1%{?dist}
Summary:        Docutils -- Python Documentation Utilities

License:        Public Domain and BSD and Python and GPLv3+
URL:            https://docutils.sourceforge.io/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit_core
BuildRequires:  python%{python3_pkgversion}-flit_scm

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove shebang from library files

sed -i -e '/#! *\/usr\/bin\/.*/{1D}' $(grep -Erl '^#!.+python' docutils)
	
# We want the licenses but don't need this build file
rm -f licenses/docutils.conf



%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/docutils
%{_bindir}/rst2html
%{_bindir}/rst2html4
%{_bindir}/rst2html5
%{_bindir}/rst2latex
%{_bindir}/rst2man
%{_bindir}/rst2odt
%{_bindir}/rst2pseudoxml
%{_bindir}/rst2s5
%{_bindir}/rst2xetex
%{_bindir}/rst2xml
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Nov 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.22.3-1
- Update to 0.22.3

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 0.21.2-3
- Add obsoletes for python3.11 package

* Wed Mar 19 2025 Odilon Sousa <osousa@redhat.com> - 0.21.2-2
- Rebuild against python3.12

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.21.2-1
- Update to 0.21.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.20.1-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.20.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.20.1-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa <osousa@redhat.com> - 0.20.1-1
- Initial package.
