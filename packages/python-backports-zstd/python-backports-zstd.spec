%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# C extension compiled with -g0 -flto (no debug symbols); suppress empty debugsource package
%global debug_package %{nil}

%global pypi_name backports.zstd
%global pypi_srcname backports_zstd
%global srcname backports-zstd

Name:           python%{python3_pkgversion}-%{srcname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Backport of the Python 3.14 compression.zstd module

License:        PSF-2.0
URL:            https://github.com/rogdham/backports.zstd
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
%{summary}


%prep
set -ex
%autosetup -n %{pypi_srcname}-%{version}
# Fix PEP 639 license field (unsupported by RHEL 9 pip)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
# Lower setuptools build requirement to match RHEL 9 (ships 68.x, not 80+)
# The >=80 requirement was driven by license-files support which we patch out above
sed -i 's/setuptools>=80/setuptools/' pyproject.toml
# Force system zstd linkage (replaces --system-zstd CLI flag)
sed -i 's/_SYSTEM_ZSTD = False/_SYSTEM_ZSTD = True/' setup.py


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt LICENSE_zstd.txt
%{python3_sitearch}/backports/zstd/
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Jul 28 2026 Odilon Sousa <osousa@redhat.com> - 1.3.0-2
- Bump release for EL10 rebuild

* Mon Mar 30 2026 Odilon Sousa <osousa@redhat.com> - 1.3.0-1
- Initial package.
