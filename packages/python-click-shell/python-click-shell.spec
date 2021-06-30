# Created by pyp2rpm-3.3.6
%global pypi_name click-shell

Name:           python-%{pypi_name}
Version:        2.1
Release:        1%{?dist}
Summary:        An extension to click that easily turns your click app into a shell utility

License:        BSD
URL:            https://github.com/clarkperkins/click-shell
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-click >= 6

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
%doc README.rst
%{python3_sitelib}/click_shell
%{python3_sitelib}/click_shell-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jun 30 2021 Evgeni Golov - 2.1-1
- Initial package.
