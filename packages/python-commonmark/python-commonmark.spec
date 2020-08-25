# Created by pyp2rpm-3.3.3
%global pypi_name commonmark

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1%{?dist}
Summary:        Python parser for the CommonMark Markdown spec

License:        BSD-3-Clause
URL:            https://github.com/rtfd/commonmark.py
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-future >= 0.14.0
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-future >= 0.14.0
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/cmark
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 25 2020 Evgeni Golov - 0.9.1-1
- Initial package.
