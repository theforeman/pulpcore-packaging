# Created by pyp2rpm-3.3.3
%global pypi_name rich

Name:           python-%{pypi_name}
Version:        10.0.1
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

License:        MIT
URL:            https://github.com/willmcgugan/rich
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-colorama < 0.5.0
Requires:       python%{python3_pkgversion}-colorama >= 0.4.0
Requires:       python%{python3_pkgversion}-commonmark < 0.10.0
Requires:       python%{python3_pkgversion}-commonmark >= 0.9.0
Requires:       python%{python3_pkgversion}-dataclasses < 0.9
Requires:       python%{python3_pkgversion}-dataclasses >= 0.7
Requires:       python%{python3_pkgversion}-pygments < 3.0.0
Requires:       python%{python3_pkgversion}-pygments >= 2.6.0
Requires:       python%{python3_pkgversion}-typing-extensions < 4.0.0
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.7.4

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

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
* Wed Mar 31 2021 Evgeni Golov 10.0.1-1
- Update to 10.0.1

* Thu Nov 05 2020 Evgeni Golov - 6.1.1-2
- Fix License tag in spec file

* Wed Sep 09 2020 Evgeni Golov 6.1.1-1
- Update to 6.1.1

* Tue Sep 01 2020 Evgeni Golov 6.0.0-1
- Update to 6.0.0

* Tue Aug 25 2020 Evgeni Golov - 5.2.1-1
- Initial package.
