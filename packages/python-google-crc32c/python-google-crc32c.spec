%global debug_package %{nil}

%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.10
%global pypi_name google-crc32c

Name:          python%{python3_pkgversion}-%{pypi_name}
Version:        1.8.0
Release:        2%{?dist}
Summary:        A python wrapper of the C library 'Google CRC32C'
BuildArch:      noarch

License:        Apache 2.0
URL:            https://github.com/googleapis/python-crc32c
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/google_crc32c-%{version}.tar.gz

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-wheel
BuildRequires: pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description
%{summary}


%prep
set -ex
%autosetup -n google_crc32c-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Defer license/authors/classifiers/dependencies/optional-dependencies to
# setup.cfg — the minimal [project] table here otherwise makes setuptools
# try (and crash on el10's 69.0.3) to reconcile them itself
sed -i '/^\[project\]/a dynamic = ["license", "authors", "classifiers", "dependencies", "optional-dependencies"]' pyproject.toml


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -npython%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/google_crc32c
%{python3_sitelib}/google_crc32c-%{version}.dist-info/


%changelog
* Wed Jul 29 2026 Odilon Sousa <osousa@redhat.com> - 1.8.0-2
- Bump release for EL10 rebuild

* Sun Mar 22 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.0-1
- Update to 1.8.0

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.7.1-1
- Update to 1.7.1

* Tue Apr 08 2025 Odilon Sousa <osousa@redhat.com> - 1.6.0-2
- Rebuild against python3.12

* Mon Sep 23 2024 Dieter Maes <dmaes@inuits.eu> - 1.6.0-1
- Initial package.
