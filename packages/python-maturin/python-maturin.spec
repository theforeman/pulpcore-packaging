%global debug_package %{nil}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name maturin

Name:           python-%{pypi_name}
Version:        1.8.3
Release:        1%{?dist}
Summary:        Build and publish crates with pyo3, cffi and uniffi bindings as well as rust binaries as python packages

License:        MIT OR Apache-2.0
URL:            https://github.com/PyO3/maturin
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.xz

#To create the vendor tarball:#
# tar xf %%{name}-%%{version}.tar.gz ; pushd %%{name}-%%{version} ; \ 
# cargo vendor --versioned-dirs --platform=x86_64-unknown-linux-gnu --version && \
# tar Jcvf ../%%{name}-%%{version}-vendor.tar.xz vendor/ ; popd

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 1.4.0
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

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
%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}


%changelog
* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.3-1
- Update to 1.8.3

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.2-1
- Update to 1.8.2

* Mon Sep 23 2024 Odilon Sousa - 1.7.1-1
- Initial package.
