%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name docutils

Name:           python-%{pypi_name}
Version:        0.20.1
Release:        4%{?dist}
Summary:        Docutils -- Python Documentation Utilities

License:        Public Domain and BSD and Python and GPLv3+
URL:            https://docutils.sourceforge.io/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
	
# Remove shebang from library files
sed -i -e '/#! *\/usr\/bin\/.*/{1D}' $(grep -Erl '^#!.+python' docutils)
	
# We want the licenses but don't need this build file
rm -f licenses/docutils.conf


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING.txt
%doc README.txt
%{_bindir}/docutils
%{_bindir}/rst2html.py
%{_bindir}/rst2html4.py
%{_bindir}/rst2html5.py
%{_bindir}/rst2latex.py
%{_bindir}/rst2man.py
%{_bindir}/rst2odt.py
%{_bindir}/rst2odt_prepstyles.py
%{_bindir}/rst2pseudoxml.py
%{_bindir}/rst2s5.py
%{_bindir}/rst2xetex.py
%{_bindir}/rst2xml.py
%{_bindir}/rstpep2html.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.20.1-4
- Remove SCL bits

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.20.1-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.20.1-2
- Build against python 3.11

* Mon Jul 17 2023 Odilon Sousa <osousa@redhat.com> - 0.20.1-1
- Initial package.
