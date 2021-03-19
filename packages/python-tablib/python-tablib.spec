# Created by pyp2rpm-3.3.3
%global pypi_name tablib

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:        MIT
URL:            https://tablib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-markuppy
Requires:       python%{python3_pkgversion}-odfpy
Requires:       python%{python3_pkgversion}-openpyxl >= 2.6.0
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-xlrd
Requires:       python%{python3_pkgversion}-xlwt

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Jun 04 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Tue Apr 28 2020 Evgeni Golov - 1.1.0-1
- Initial package.
