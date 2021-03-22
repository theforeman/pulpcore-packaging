# Created by pyp2rpm-3.3.3
%global pypi_name Markdown
%global srcname markdown

Name:           python-%{srcname}
Version:        3.3.4
Release:        1%{?dist}
Summary:        Python implementation of Markdown

License:        BSD License
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-importlib-metadata
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.md
%{_bindir}/markdown_py
%{python3_sitelib}/markdown
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 3.3.4-1
- Update to 3.3.4

* Thu Oct 29 2020 Evgeni Golov 3.3.3-1
- Update to 3.3.3

* Tue Jun 23 2020 Evgeni Golov - 3.2.2-1
- Initial package.
