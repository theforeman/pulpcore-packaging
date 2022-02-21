# Created by pyp2rpm-3.3.7
%global pypi_name soupsieve

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        1%{?dist}
Summary:        A modern CSS selector implementation for Beautiful Soup

License:        MIT License
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Feb 21 2022 Odilon Sousa <osousa@redhat.com> - 2.3.1-1
- Initial package.
