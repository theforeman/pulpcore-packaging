# Created by pyp2rpm-3.3.3
%global pypi_name typing

Name:           python-%{pypi_name}
Version:        3.7.4.3
Release:        1%{?dist}
Summary:        Type Hints for Python

License:        PSF
URL:            https://docs.python.org/3/library/typing.html
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

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
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 20 2020 Evgeni Golov 3.7.4.3-1
- Update to 3.7.4.3

* Wed Mar 18 2020 Samir Jha - 3.7.4.1-1
- Initial package.
